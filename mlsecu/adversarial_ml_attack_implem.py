from numpy import inf

def fgsm_attack_svm_2c(classifier, orig_point, dist_function, step=None, epsilon=inf, max_step=200):
    """
        Implement a simplified variant of FGSM - Fast Gradient Signed Method.
        The method identifies a possible attack launched from a given origin point.
        Required supported configuration is: 2-class SVM classifier.
        FGSM works as follows:

        as long as the distance between attack point and origin point is less than epsilon
        and the number of steps performed is less than max_step
        move in the direction of the gradient

        For SVM with linear kernel for instance, the direction of maximal gradient is given by
        classifier.coef_ (beware: this is not the case for other SVM kernels).


        :param classifier: the trained classifier model
        :param orig_point: the origin point for the attack
        :param dist_function: the distance function to be used
        :param step: the step for gradient movement
        :param epsilon: the maximal alteration of the data
        :param max_step: the maximal number of steps
        :return: the crafted data point for the attack, as well as the actual alteration, if any
    """
    data_point = orig_point.copy()
    orig_class = classifier.predict(data_point.reshape(1, -1))[0]
    new_class = orig_class
    current_eps = dist_function(data_point,orig_point)
    attack_info = None
    i = 0
    
    data_points_pos = [data_point]
    while orig_class == new_class:
        if current_eps < epsilon and i < max_step:
            grad =  classifier.coef_[0]
            data_point = data_point + step *  grad
            data_points_pos.append(data_point)
            new_class = classifier.predict(data_point.reshape(1, -1))[0]
            current_eps = dist_function(data_point,orig_point)
            attack_info = data_point, current_eps
        else:
            attack_info = (None, None)
            
            if current_eps > epsilon:
                print("Attack failed: epsilon exceeded",current_eps)
            if i >= max_step:
                print("Attack failed: max step exceeded")
            break
        i += 1
    return attack_info