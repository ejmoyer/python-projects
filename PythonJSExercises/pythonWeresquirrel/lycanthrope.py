# The Lycanthrope's Log
journal = []

def add_Entry(events, squirrel):
    journal.append({events, squirrel})

add_Entry(['work', 'touched tree', 'pizza', 'running',
            'television'], False)
add_Entry(['work', 'ice cream', 'cauliflower', 'lasagna',
            'touched tree', 'brushed teeth'], False)
add_Entry(['weekend', 'cycling', 'break', 'peanuts'
            'beer'], True)
# Computing Correlation
def phi(table):
    return ((table[3] * table[0] - table[2] * table[1]) /
        math.sqrt((table[2] + table[3]) *
                  (table[0] + table[1]) *
                  (table[1] + table[3]) *
                  (table[0] + table[2])))

def table_For(event, journal):
    
