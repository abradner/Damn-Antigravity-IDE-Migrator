import os
import sys
from dataclasses import dataclass

@dataclass
class AppPaths:
    # App configuration folders (contains settings.json and state.vscdb)
    old_roaming: str
    new_roaming: str
    
    # User Profile dot-folders (contains extensions and argv.json)
    old_dot: str
    new_dot: str
    
    # Gemini folders (contains conversations and brain states)
    old_gemini: str
    new_gemini: str

def resolve_paths() -> AppPaths:
    """Dynamically resolves migration paths on the user's system (cross-platform)."""
    user_home = os.path.expanduser("~")

    if sys.platform == "win32":
        config_base = os.environ.get("APPDATA")
        if not config_base:
            raise EnvironmentError("APPDATA environment variable is not defined.")
    elif sys.platform == "darwin":
        config_base = os.path.join(user_home, "Library", "Application Support")
    else:
        # Linux and other POSIX systems follow the XDG Base Directory spec
        config_base = os.environ.get("XDG_CONFIG_HOME", os.path.join(user_home, ".config"))

    return AppPaths(
        old_roaming=os.path.join(config_base, "Antigravity"),
        new_roaming=os.path.join(config_base, "Antigravity IDE"),
        old_dot=os.path.join(user_home, ".antigravity"),
        new_dot=os.path.join(user_home, ".antigravity-ide"),
        old_gemini=os.path.join(user_home, ".gemini", "antigravity"),
        new_gemini=os.path.join(user_home, ".gemini", "antigravity-ide")
    )
