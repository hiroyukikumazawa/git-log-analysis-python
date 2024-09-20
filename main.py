import subprocess
import os
from datetime import datetime, timedelta


def clone_repo_if_not_exist(repo_url, repo_path):
    if not os.path.isdir(repo_path):
        clone_result = subprocess.run(
            ['git', 'clone', repo_url, repo_path],
            stdout=subprocess.PIPE,
            text=True
        )

        if clone_result.returncode != 0:
            return False
        return True

def pull_latest_commit(repo_path):
    pull_result = subprocess.run(
        ['git', 'pull'],
        cwd=repo_path,
        stdout=subprocess.PIPE,
        text=True
    )
    print(pull_result, 'aaa')
    if pull_result.returncode != 0:
        return False
    return True

def main():
    today = datetime.now()
    three_months_ago = today - timedelta(days=90)
    since_date = three_months_ago.strftime("%Y-%m-%d")
    
    git_logs = subprocess.run(
        ['git', 'log', f'--since={since_date}', '--pretty=format:%an'],
        cwd='/home/reef/ex-github-repos/cpython',
        # cwd='/home/reef/subnets/prompting',
        stdout=subprocess.PIPE,
        text=True
    )

    if git_logs.returncode != 0:
        raise
    
    print(len(git_logs.stdout.splitlines()))
    print(len(set(git_logs.stdout.splitlines())))

if __name__ == "__main__":
    main()