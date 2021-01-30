import string


def clean_string_iswc(iswc):
    """

    :param iswc:
    :return:
    """
    # Benchmarking: https://towardsdatascience.com/how-to-efficiently-remove-punctuations-from-a-string-899ad4a059fb
    table_dict = str.maketrans('', '', string.punctuation)
    iswc_mod = iswc.translate(table_dict)
    return iswc_mod
