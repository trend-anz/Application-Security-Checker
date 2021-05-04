import boto3
from typing import List, Dict, Any


def _get_lambdas() -> List[Dict[Any, Any]]:
    """Get Lambda configurations from an account.

    Returns:
        list: List of Lambdas and their configurations

    """
    lambdas = []

    client = boto3.client("lambda")
    paginator = client.get_paginator("list_functions")
    page_iterator = paginator.paginate()

    for page in page_iterator:
        lambdas += page["Functions"]

    return lambdas


def check_protection() -> Dict[str, bool]:
    """Check whether Lambdas are running Application Security or not.

    Returns:
        dict: Lambda names & their protection status.

    """
    status = {}

    lambda_functions = _get_lambdas()

    for lambda_function in lambda_functions:
        lambda_name = lambda_function["FunctionName"]
        get_lambda_variables = lambda_function.get("Environment")

        if not get_lambda_variables:
            status[lambda_name] = False
            continue

        lambda_variables = get_lambda_variables["Variables"]
        protection_status = True if ("TREND_AP_KEY" and "TREND_AP_SECRET") in lambda_variables else False
        status[lambda_name] = protection_status

    return status


def main() -> None:
    """Run Application Security Checker.

    Returns:
        None

    """
    protection_status = check_protection()

    protected_count = 0
    unprotected_count = 0

    for lambda_name, lambda_status in protection_status.items():
        print(f"{lambda_name}: {lambda_status}")

        if lambda_status:
            protected_count += 1

        else:
            unprotected_count += 1

    total_count = protected_count + unprotected_count
    unprotected_percentage = round(100 * float(unprotected_count) / float(total_count), 2)

    print(f"\n{unprotected_count}/{total_count} ({unprotected_percentage}%) of Lambdas are unprotected.")


if __name__ == "__main__":
    main()
