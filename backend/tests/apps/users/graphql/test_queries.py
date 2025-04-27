from unittest.mock import AsyncMock, patch

from piccolo.apps.user.tables import BaseUser


class TestUserQueries:
    @patch.object(BaseUser, "objects")
    async def test_get_user_by_id(self, mock_objects, graphql_client):
        mock_user = BaseUser(
            id=1,
            username="testuser",
            first_name="Test",
            last_name="User",
            email="test@example.com",
        )
        mock_objects.return_value.get = AsyncMock(return_value=mock_user)

        query = """
        query GetUser($id: ID!) {
            user(id: $id) {
                id
                username
                firstName
                lastName
                email
            }
        }
        """

        result = await graphql_client.query(query, variables={"id": "1"})

        assert "errors" not in result
        assert "data" in result

        user_data = result["data"]["user"]
        assert user_data is not None
        assert user_data["id"] == "1"
        assert user_data["username"] == "testuser"
        assert user_data["firstName"] == "Test"
        assert user_data["lastName"] == "User"
        assert user_data["email"] == "test@example.com"

        assert mock_objects.return_value.get.called
        assert mock_objects.return_value.get.call_count == 1

    @patch.object(BaseUser, "objects")
    async def test_get_user_by_id_not_found(self, mock_objects, graphql_client):
        mock_objects.return_value.get = AsyncMock(return_value=None)

        query = """
        query GetUser($id: ID!) {
            user(id: $id) {
                id
                username
            }
        }
        """

        result = await graphql_client.query(query, variables={"id": "999"})

        assert "errors" in result
        assert len(result["errors"]) == 1
        assert "User with id 999 not found" in result["errors"][0]["message"]
