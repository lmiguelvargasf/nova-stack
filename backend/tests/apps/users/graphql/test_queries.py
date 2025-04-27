from unittest.mock import AsyncMock, patch

import pytest
from piccolo.apps.user.tables import BaseUser


@pytest.mark.asyncio
class TestUserQueries:
    @patch.object(BaseUser, "objects")
    async def test_get_user_by_id(self, mock_objects, test_client):
        # Setup mock database response
        mock_user = BaseUser(
            id=1,
            username="testuser",
            first_name="Test",
            last_name="User",
            email="test@example.com",
        )

        # Configure mock
        mock_objects.return_value.get = AsyncMock(return_value=mock_user)

        # Define query
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

        # Execute query with variables
        response = await test_client.post(
            "/graphql", json={"query": query, "variables": {"id": "1"}}
        )

        # Assert successful response
        assert response.status_code == 200

        # Get result data
        result = response.json()
        assert "errors" not in result
        assert "data" in result

        # Assert expected data
        user_data = result["data"]["user"]
        assert user_data is not None
        assert user_data["id"] == "1"
        assert user_data["username"] == "testuser"
        assert user_data["firstName"] == "Test"
        assert user_data["lastName"] == "User"
        assert user_data["email"] == "test@example.com"

        # Verify mock was called once
        assert mock_objects.return_value.get.called
        assert mock_objects.return_value.get.call_count == 1

    @patch.object(BaseUser, "objects")
    async def test_get_user_by_id_not_found(self, mock_objects, test_client):
        # Configure mock to return None
        mock_objects.return_value.get = AsyncMock(return_value=None)

        # Define query
        query = """
        query GetUser($id: ID!) {
            user(id: $id) {
                id
                username
            }
        }
        """

        # Execute query with non-existent ID
        response = await test_client.post(
            "/graphql", json={"query": query, "variables": {"id": "999"}}
        )

        # Assert successful HTTP response (GraphQL errors are still 200 OK)
        assert response.status_code == 200

        # Check for GraphQL error
        result = response.json()
        assert "errors" in result
        assert len(result["errors"]) == 1
        assert "User with id 999 not found" in result["errors"][0]["message"]
