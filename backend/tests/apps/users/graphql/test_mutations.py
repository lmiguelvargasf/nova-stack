from unittest.mock import AsyncMock, patch

from piccolo.apps.user.tables import BaseUser


class TestUserMutations:
    @patch("src.backend.apps.users.graphql.mutations.BaseUser.objects")
    async def test_create_user_success(self, mock_objects, graphql_client):
        # Setup mock to return no existing user
        mock_get = AsyncMock(return_value=None)
        mock_objects.return_value.get = mock_get

        # Create a test user with a controlled ID
        with patch.object(BaseUser, "save", new_callable=AsyncMock) as mock_save:
            # Set the ID directly in the BaseUser.__init__ method
            original_init = BaseUser.__init__

            def patched_init(self, *args, **kwargs):
                original_init(self, *args, **kwargs)
                self.id = 1

            with patch.object(BaseUser, "__init__", patched_init):
                # Execute the mutation
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

        assert "data" in result
        assert "createUser" in result["data"]
        assert result["data"]["createUser"] == {
            "id": "1",
            "username": "newuser",
            "firstName": "New",
            "lastName": "User",
            "email": "new@example.com",
        }

        mock_get.assert_called_once()
        mock_save.assert_called_once()

    @patch.object(BaseUser, "objects")
    async def test_create_user_already_exists(self, mock_objects, graphql_client):
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
