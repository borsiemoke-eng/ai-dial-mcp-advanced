from typing import Any

from mcp_server.tools.users.base import BaseUserServiceTool


class DeleteUserTool(BaseUserServiceTool):

    @property
    def name(self) -> str:
        #Provide tool name as `delete_users`
        return "delete_user"

    @property
    def description(self) -> str:
        #Provide description of this tool
        return "Deletes user by user_id"

    @property
    def input_schema(self) -> dict[str, Any]:
        # Provide tool params Schema. This tool applies user `id` (number) as a parameter and it is required
        return {
            "type": "object",
            "properties": {
                "id": {
                    "type": "number",
                    "description": "User ID"
                }
            },
            "required": ["id"]
        }

    async def execute(self, arguments: dict[str, Any]) -> str:
        # 1. Get int `id` from arguments
        user_id = int(arguments["id"])
        # 2. Call user_client delete_user and return its results (it is async, don't forget to await)
        return await self._user_client.delete_user(user_id)