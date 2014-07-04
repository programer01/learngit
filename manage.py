#hello everyone ,this is a test for git.
#this is a second test.
#!/usr/bin/env python
import os


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "HomeworkManager.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
