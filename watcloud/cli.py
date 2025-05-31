import argparse
from .commands import status, quota, maintaince  # Adjust imports as needed

def main():
    parser = argparse.ArgumentParser(
        description="WatCloud CLI - Manage your cloud cluster"
    )
    subparsers = parser.add_subparsers(
        title="Commands",
        dest="command",
        required=True,
        help="Available commands"
    )

    # Status command
    status_parser = subparsers.add_parser("status", help="Show cluster status")
    status_parser.set_defaults(func=status.get_cluster_status)

    # Quota command
    quota_parser = subparsers.add_parser("quota", help="Manage quotas")
    quota_subparsers = quota_parser.add_subparsers(dest="subcommand", required=True)

    # quota list
    list_parser = quota_subparsers.add_parser("list", help="lists all quota usage")
    list_parser.set_defaults(func=quota.list_quota_usage)
    
    # quota disk
    disk_parser = quota_subparsers.add_parser("disk", help="returns the disk status")
    disk_parser.add_argument("disk", help="Node to mark under maintenance")
    disk_parser.set_defaults(func=quota.check_disk_usage)
    quota_args = parser.parse_args()

    # Maintenance command
    maintaince_parser = subparsers.add_parser("maintenance", help="Manage maintenance status")
    maintaince_subparsers = maintaince_parser.add_subparsers(dest="subcommand", required=True)

    # maintenance mark
    mark_parser = maintaince_subparsers.add_parser("mark", help="Mark node under maintenance")
    mark_parser.add_argument("node_name", help="Node to mark under maintenance")
    mark_parser.add_argument("--until", help="Maintenance end time (optional)")
    mark_parser.set_defaults(func=maintaince.mark_maintenance)

    # maintenance remove
    remove_parser = maintaince_subparsers.add_parser("remove", help="Remove maintenance status")
    remove_parser.add_argument("node_name", help="Node to remove maintenance from")
    remove_parser.set_defaults(func=maintaince.remove_maintenance)

    # maintenance check
    remove_parser = maintaince_subparsers.add_parser("check", help="check maintenance status")
    remove_parser.add_argument("node_name", help="Node to check maintenance from")
    remove_parser.set_defaults(func=maintaince.print_under_maintenance)
    maintaince_args = parser.parse_args()

    # Call the function associated with the chosen command
    args = quota_args + maintaince_args

    if hasattr(args, "func"):
        if "subcommand" in args:
            all_args = vars(args)

            filtered_args = {k: v for k, v in all_args.items() if k not in ("command", "subcommand", "func")}

            args.func(**filtered_args)
        else:
            args.func()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()