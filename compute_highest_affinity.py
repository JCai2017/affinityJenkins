# No need to process files and manipulate strings - we will
# pass in lists (of equal length) that correspond to
# sites views. The first list is the site visited, the second is
# the user who visited the site.

# See the test cases for more details.


def highest_affinity(site_list, user_list, time_list):
    # Returned string pair should be ordered by dictionary order
    # I.e., if the highest affinity pair is "foo" and "bar"
    # return ("bar", "foo").
    site_visit = dict()
    for site in site_list:
        site_visit[site] = []

    for key in site_visit:
        for key2 in site_visit:
            if key != key2:
                shared = 0
                for usr in site_visit[key]:
                    if usr in site_visit[key2]:
                        shared += 1
                if shared >= best_shared:
                    best_tuple = (key2, key)
                    best_shared = shared

        for key2 in site_visit:
            if key != key2:
                shared = 0
                for usr in site_visit[key]:
                    if usr in site_visit[key2]:
                        shared += 1
                if shared >= best_shared:
                    best_tuple = (key2, key)
                    best_shared = shared

        for key2 in site_visit:
            if key != key2:
                shared = 0
                for usr in site_visit[key]:
                    if usr in site_visit[key2]:
                        shared += 1
                if shared >= best_shared:
                    best_tuple = (key2, key)
                    best_shared = shared


    for i in range(0, len(site_list)):
            site_visit[site_list[i]].append(user_list[i])

    best_tuple = ("", "")
    best_shared = -1
    for key in site_visit:
        for key2 in site_visit:
            if key != key2:
                shared = 0
                for usr in site_visit[key]:
                    if usr in site_visit[key2]:
                        shared += 1
                if shared >= best_shared:
                    best_tuple = (key2, key)
                    best_shared = shared

    return best_tuple
