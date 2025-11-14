#!/usr/bin/env python3
"""
LeetCode Daily Question Fetcher
Fetches the daily coding challenge from LeetCode using GraphQL API
"""

import json
import requests
import sys
from datetime import datetime


class LeetCodeFetcher:
    """Fetches daily question from LeetCode"""

    GRAPHQL_URL = "https://leetcode.com/graphql"

    # GraphQL query to get daily coding challenge
    DAILY_QUESTION_QUERY = """
    query questionOfToday {
        activeDailyCodingChallengeQuestion {
            date
            link
            question {
                questionId
                questionFrontendId
                title
                titleSlug
                content
                difficulty
                exampleTestcases
                topicTags {
                    name
                    slug
                }
                codeSnippets {
                    lang
                    langSlug
                    code
                }
                hints
                solution {
                    id
                    canSeeDetail
                    paidOnly
                }
            }
        }
    }
    """

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })

    def fetch_daily_question(self):
        """Fetch the daily coding challenge"""
        try:
            response = self.session.post(
                self.GRAPHQL_URL,
                json={'query': self.DAILY_QUESTION_QUERY},
                timeout=10
            )
            response.raise_for_status()

            data = response.json()

            if 'errors' in data:
                print(f"GraphQL errors: {data['errors']}", file=sys.stderr)
                return None

            daily_question = data.get('data', {}).get('activeDailyCodingChallengeQuestion')

            if not daily_question:
                print("No daily question found", file=sys.stderr)
                return None

            return self._process_question(daily_question)

        except requests.exceptions.RequestException as e:
            print(f"Error fetching from LeetCode: {e}", file=sys.stderr)
            return None
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON response: {e}", file=sys.stderr)
            return None

    def _process_question(self, daily_question):
        """Process and structure the question data"""
        question = daily_question.get('question', {})

        # Get Python code snippet (default to Python3)
        python_code = ""
        for snippet in question.get('codeSnippets', []):
            if snippet.get('langSlug') in ['python3', 'python']:
                python_code = snippet.get('code', '')
                break

        return {
            'date': daily_question.get('date'),
            'title': question.get('title', 'Unknown Title'),
            'title_slug': question.get('titleSlug', ''),
            'question_id': question.get('questionFrontendId', ''),
            'difficulty': question.get('difficulty', 'Unknown'),
            'content': question.get('content', ''),
            'link': f"https://leetcode.com{daily_question.get('link', '')}",
            'topics': [tag.get('name') for tag in question.get('topicTags', [])],
            'hints': question.get('hints', []),
            'code_template': python_code,
            'example_testcases': question.get('exampleTestcases', ''),
        }


def main():
    """Main function"""
    fetcher = LeetCodeFetcher()
    question_data = fetcher.fetch_daily_question()

    if question_data:
        # Output as JSON for the next script to consume
        print(json.dumps(question_data, indent=2, ensure_ascii=False))
        return 0
    else:
        print("Failed to fetch daily question", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
