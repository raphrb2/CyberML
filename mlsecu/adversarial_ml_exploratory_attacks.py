def get_adversarial_points(classifier, candidates, attack, dist_function, epsilon):
    """"
    Get the list of data points from which a successful adversarial attack of radius epsilon or less can be performed.
    This list entails all candidates for which given attack can be performed in given epsilon

    :param classifier: the classifier to be exploited
    :param candidates: the list of candidate points from which the attack can start.
    :param attack: the attack function
    :param epsilon: the maximum alteration
    :param dist_function: the distance function to be used
    :return: original_points the original data points which are sources of the attack with the smallest
    alteration, altered_points the crafted data points for the attack, as well as
    adv_epsilons the actual alterations, if any.
    """
    original_points = []
    altered_points = []
    adv_epsilons = []
    step = 0.01

    for candidate in candidates:
        adversarial_ex, current_epsilon = attack(classifier, candidate, dist_function, step=step, epsilon=epsilon)
        if adversarial_ex is not None:
            original_points.append(candidate)
            altered_points.append(adversarial_ex)
            adv_epsilons.append(current_epsilon)
    return original_points, altered_points, adv_epsilons
    

def get_smallest_alteration(classifier, candidates, attack, dist_function):
    """
        Get the smallest possible alteration for an adversarial attack on a given classifier for a given attack.
        The smallest alteration is obtained by performing the given attack against each candidate, and
        taking the better option.
        Required supported configuration is: 2-class SVM classifier.

        :param classifier: the classifier to be exploited
        :param candidates: the list of candidate points from which the attack can start.
        :param attack: the attack function
        :param dist_function: the distance function to be used
        :return: original_point the original data point source of the attack with the smallest alteration,
        altered_point the crafted data point for the attack, as well as adv_epsilon the actual alteration, if any
    """
    origin_point, altered_point = None, None
    adv_epsilon = float('inf')
    step = 0.01

    for candidate in candidates:
        adversarial_example, current_epsilon = attack(classifier, candidate, dist_function, step=step)

        if adversarial_example is not None and current_epsilon < adv_epsilon:
            origin_point, altered_point, adv_epsilon = candidate, adversarial_example, current_epsilon

    return origin_point, altered_point, adv_epsilon