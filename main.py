def parse(query: str) -> dict:
    if '?' in query:
        my_str = query.split('?')[-1]
        my_split_list = my_str.split('&')
        my_split_list = list(filter(None, my_split_list))
        my_dict = {}
        for i in my_split_list:
            my_key, my_value = i.split('=')[0], i.split('=')[-1]
            my_dict[my_key] = my_value
    else:
        my_dict = {}
    return my_dict


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}


def parse_cookie(query: str) -> dict:
    if ';' in query:
        my_split_list = query.split(';')
        my_split_list = list(filter(None, my_split_list))
        my_dict = {}
        for i in my_split_list:
            index = i.find('=')
            my_key, my_value = i[0: index], i[(index + 1):]
            my_dict[my_key] = my_value
    else:
        my_dict = {}
    return my_dict


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
