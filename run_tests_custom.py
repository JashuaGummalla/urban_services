import sys
import os
import django

# Add project root to path
sys.path.append(os.getcwd())

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "urban_services.settings")
django.setup()

from django.test.runner import DiscoverRunner

print("Starting tests...")
with open('debug_output.txt', 'w') as f:
    sys.stdout = f
    sys.stderr = f
    runner = DiscoverRunner(verbosity=2, interactive=False)
    failures = runner.run_tests(['bookings'])
print(f"Tests finished with {failures} failures.")
