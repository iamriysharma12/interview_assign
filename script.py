
import shlex
import croniter
from prettytable import PrettyTable
import sys

def parse_cron(cron_string):
    fields = shlex.split(cron_string)
    cron = croniter.croniter(' '.join(fields[:-1]), start_time=0)
    table = PrettyTable(['Field', 'Time'])
    table.align['Time'] = 'l'
    table.align['Field'] = 'l'
    fields_name = ['minute', 'hour', 'day of month', 'month', 'day of week', 'command']
    for i, field in enumerate(fields):
        times = []
        if '*' in field:
            times = 'Any'
        elif '/' in field:
            times = field
        elif ',' in field:
            times = field.split(',')
        elif '-' in field:
            times = field
        else:
            times = field
        table.add_row([fields_name[i], times])
    table.add_row(['command', fields[-1]])
    return table

if __name__ == "__main__":
    cron_string = sys.argv[1]
    table = parse_cron(cron_string)
    print(table)


