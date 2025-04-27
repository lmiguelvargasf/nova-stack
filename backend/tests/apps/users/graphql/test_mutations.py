from unittest.mock import AsyncMock, patch

from piccolo.apps.user.tables import BaseUser


class TestUserMutations:
    @patch.object(BaseUser, "objects")
    async def test_create_user_success(self, mock_objects, graphql_client):
        # Mock that no user exists with this username
        mock_objects.return_value.get = AsyncMock(return_value=None)

        # We'll patch the save method but not try to modify the ID
        mock_save = AsyncMock()

        with patch.object(BaseUser, "save", mock_save):
            mutation = """
            mutation CreateUser($userInput: UserInput!) {
                createUser(userInput: $userInput) {
                    id
                    username
                    firstName
                    lastName
                    email
                }
            }
            """

            variables = {
                "userInput": {
                    "username": "newuser",
                    "firstName": "New",
                    "lastName": "User",
                    "email": "new@example.com",
                }
            }

            result = await graphql_client.mutation(mutation, variables=variables)

            assert "errors" not in result, f"Errors in response: {result.get('errors')}"
            assert "data" in result

            user_data = result["data"]["createUser"]
            assert user_data is not None
            # Revert to expecting "DEFAULT" as the ID in the test environment
            assert user_data["id"] == "DEFAULT"
            assert user_data["username"] == "newuser"
            assert user_data["firstName"] == "New"
            assert user_data["lastName"] == "User"
            assert user_data["email"] == "new@example.com"

            # Verify that save was called
            assert mock_save.called

    @patch.object(BaseUser, "objects")
    async def test_create_user_already_exists(self, mock_objects, graphql_client):
        # Mock that a user already exists with this username
        existing_user = BaseUser(
            id=1,
            username="existinguser",
            first_name="Existing",
            last_name="User",
            email="existing@example.com",
        )
        mock_objects.return_value.get = AsyncMock(return_value=existing_user)

        mutation = """
        mutation CreateUser($userInput: UserInput!) {
            createUser(userInput: $userInput) {
                id
                username
            }
        }
        """

        variables = {
            "userInput": {
                "username": "existinguser",
                "firstName": "Test",
                "lastName": "User",
                "email": "test@example.com",
            }
        }

        result = await graphql_client.mutation(mutation, variables=variables)

        assert "errors" in result
        assert len(result["errors"]) == 1
        assert (
            "User with username 'existinguser' already exists"
            in result["errors"][0]["message"]
        )
