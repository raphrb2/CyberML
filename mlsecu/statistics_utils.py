import math

def get_euclidian_dist(a, b):
    """get the euclidian distance between two points
        
        :param p1: first point
        :param p2: second point
        :return: the euclidian distance between the two points
    """
    if len(a) != len(b):
        return None
    
    diff_square_sum = sum((a_i - b_i) ** 2 for a_i, b_i in zip(a, b))
    return math.sqrt(diff_square_sum)


def get_l0(p1, p2):
    """
    get the l0 distance between two points
        
        :param p1: first point
        :param p2: second point
        :return: the l0 distance between the two points
     """
    if len(p1) != len(p2):
        return None
    return sum(a != b for a, b in zip(p1, p2))


def get_l1(p1, p2):
    """
    get the l1 distance between two points
    
    :param p1: first point
    :param p2: second point
    :return: the l1 distance between the two points
    """
    if len(p1) != len(p2):
        return None
    return sum(abs(a_i - b_i) for a_i, b_i in zip(p1, p2))


def get_l2(p1, p2):
    """
    get the l2 distance between two points
    
    :param p1: first point
    :param p2: second point
    :return: the l2 distance between the two points
    """
    if len(p1) != len(p2):
        return None
    diff_square_sum = sum((a_i - b_i) ** 2 for a_i, b_i in zip(p1, p2))
    return diff_square_sum


def get_l_inf(p1, p2):
    """"
    get the l_inf distance between two points
    
    :param p1: first point
    :param p2: second point
    :return: the l_inf distance between the two points
    """
    if len(p1) != len(p2):
        return None
    return max(abs(a - b) for a, b in zip(p1, p2))