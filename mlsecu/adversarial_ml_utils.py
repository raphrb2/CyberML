def get_astute_accuracy_from_attack_points(orig_points, orig_labels, points_with_successful_attacks, class_label):
    """
    Retrieves the astute accuracy of a classifier based on the list of original data points, and the list of
    `clipped' data points, i.e. the list of points including successful attacks.
    The number of different attacks is considered (if a point appears 2 times, it is only considered once).

    :param orig_points: the data points of the original distribution
    :param orig_labels: the original class labels
    :param points_with_successful_attacks: the data points after the attacks, where points susceptible of successful
    attack are replaced by the attack point
    :param class_label: the class for which the astuteness is computed
    :return: the astute accuracy
    """
    relevant_orig_points = [point for point, label in zip(orig_points, orig_labels) if label == class_label]

    unique_attacks = set(tuple(point) for point in points_with_successful_attacks)

    successfully_attacked_points = [point for point in relevant_orig_points if tuple(point) in unique_attacks]

    astute_accuracy = len(successfully_attacked_points) / len(relevant_orig_points) if relevant_orig_points else 0

    return astute_accuracy
    
 


def get_astute_accuracy_from_success_array(orig_labels, success_array, class_label):
    """"
    Retrieves the astute accuracy of a classifier for a given class, based on the success array for the attack.
    :param orig_labels: the original class labels
    :param success_array: the array identifying the successful adversarial attacks for a data point set of same length
    :param class_label: the class for which the astuteness is computed
    :return: the astute accuracy

    """
    if len(orig_labels) != len(success_array):
        return None

    
    target_class_instances = [label for label in orig_labels if label == class_label]

    unsuccessful_attacks = sum(1 for label, success in zip(orig_labels, success_array) if label == class_label and success == 0)

    astute_accuracy = unsuccessful_attacks / len(target_class_instances) if target_class_instances else 0

    return astute_accuracy

 
def get_robust_accuracy_from_attack_points(orig_points, points_with_successful_attacks):
    """
    Retrieves the robust accuracy of a classifier based on the list of original data points, and the list of
    `clipped' data points, i.e. the list of points including successful attacks.
    The number of different attacks is considered (if a point appears 2 times, it is only considered once).

    :param orig_points: the data points of the original distribution
    :param points_with_successful_attacks: the data points after the attacks, where points susceptible of successful
    attack are replaced by the attack point
    :return: the robust accuracy
    """
    if len(orig_points) != len(points_with_successful_attacks):
        return None

    num_successful_attacks = sum(1 for orig, attacked in zip(orig_points, points_with_successful_attacks) if orig != attacked)
    
    robust_accuracy = 1 - (num_successful_attacks / len(orig_points))
    
    return robust_accuracy

def get_robust_accuracy_from_success_array(success_array):
    """
    Retrieves the robust accuracy of a classifier based on the success array for the attack.
 
    :param success_array: the array identifying the successful adversarial attacks for a data point set of same length
    :return: the robust accuracy
    """
    
    num_successful_attacks = sum(success_array)
    
    robust_accuracy = 1 - (num_successful_attacks / len(success_array))
    
    return robust_accuracy


