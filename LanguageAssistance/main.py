import os
import warnings


warnings.filterwarnings("ignore")
os.environ['TRANSFORMERS_VERBOSITY'] = 'error'

from app.profile import load_profile, create_profile_interactive
from app.daily_practice import run_daily_session

if __name__ == "__main__":
    profile = load_profile()
    if not profile:
        profile = create_profile_interactive()
    run_daily_session(profile)
