import string


def clean_string_iswc(iswc):
    """
    Delete all puctuation characters from the string.
    :param iswc:
    :return: iswc_mod ()
    """
    # References: https://towardsdatascience.com/how-to-efficiently-remove-punctuations-from-a-string-899ad4a059fb
    table_dict = str.maketrans('', '', string.punctuation)
    iswc_mod = iswc.translate(table_dict)
    return iswc_mod
