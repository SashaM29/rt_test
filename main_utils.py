def proc_csv():
    """
    Reads csv file and creates structures necessary for work

    Returns:
        cats {dict} - Categories
        cats_max_show {dict} - Maximum shows per category
        objects_num_show {dict} - Number of show of each object
        objects_power {dict} - Product of the number of shows of an object by the number of its categories
        objects_num_cat {dict} - Number of categories for each object
    """
    cats = dict()
    cats_max_show = dict()
    objects_num_show = dict()
    objects_power = dict()
    objects_num_cat = dict()

    file = open('conf.csv', 'r')
    while True:
        line = file.readline()
        if not line:
            break
        line = line.strip().split(';')
        objects_num_show[line[0]] = line[1]
        objects_power[line[0]] = int(line[1]) * (len(line) - 2)
        objects_num_cat[line[0]] = int(len(line) - 2)
        for k in range(len(line) - 2):
            if line[k + 2] not in cats:
                cats[line[k + 2]] = line[0]
            else:
                cats[line[k + 2]] = cats[line[k + 2]] + '&' + line[0]

    for key in cats:
        temp = str(cats[key]).split('&')
        N = 0
        for k in temp:
            N = N + int(objects_num_show[k])
        cats_max_show[key] = N

    file.close()

    return cats, cats_max_show, objects_num_show, objects_power, objects_num_cat


def get_cat(request, cats):
    """
    Returns the list of categories in the request.
    If the query is empty, return all available categories

    Arguments:
        request {list} - Categories in request
        cats {dict} - All available categories

    Returns:
        cat {list} - Available categories to show
    """
    if len(request) > 0:
        cat = request.getlist('category')
    else:
        cat = list(cats)
    return cat


def get_object_to_show(req_cat, cats_max_show, cats, objects_power):
    """
        Returns the address of the object to show

        Arguments:
            req_cat {list} - Available categories to show
            cats_max_show {dict} - Maximum shows per category
            cats {dict} - Categories
            objects_power {dict} - Product of the number of shows of an object by the number of its categories

        Returns:
            response {str} - Available categories
        """
    temp = []
    for k in req_cat:
        temp.append(cats_max_show[k])
    max_val = max(temp)
    idx_max = temp.index(max_val)
    objects_to_show = cats[req_cat[idx_max]].split('&')
    temp = []
    for k in objects_to_show:
        if objects_power[k] == 0:
            temp.append(max(objects_power.values()) + 1)
        else:
            temp.append(objects_power[k])
    min_val = min(temp)
    idx_min = temp.index(min_val)
    response = objects_to_show[idx_min]
    return response

