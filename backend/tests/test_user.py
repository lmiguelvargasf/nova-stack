"""
TODO: These tests cover basic BaseUser functionality likely already tested
in piccolo_admin itself. Remove these tests once actual application-specific
tests involving database transactions are implemented.
"""

from typing import ClassVar

from piccolo.testing.test_case import AsyncTableTest
from piccolo_admin.endpoints import BaseUser


class TestBaseUser(AsyncTableTest):
    tables: ClassVar[list] = [BaseUser]

    async def test_create_user(self):
        """Test creating a user and retrieving it"""
        test_username = "testuser"
        test_password = "TestPassword123"

        user = await BaseUser.create_user(
            username=test_username, password=test_password
        )

        assert user.id is not None
        assert user.username == test_username
        retrieved_user = await BaseUser.objects().get(
            BaseUser.username == test_username
        )
        assert retrieved_user.id == user.id
        assert retrieved_user.username == test_username
