def sample_responses(input_txt):
    user_message = str(input_txt).lower()

    if user_message in ('hello', 'hi'):
        return 'fine'

    if user_message in ('123'):
        return '456'

    if user_message in ('time'):
        return 'now'

    return 'elli'


