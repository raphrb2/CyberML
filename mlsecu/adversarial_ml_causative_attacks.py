def move_decision_frontier(classifier, poisoning_points, target_class, point_to_hide, max_step=200):
    """
        Moves the decision frontier until it hides some data point.
        Supported classifier: MLP.

        :param classifier: the classifier to be exploited. Needs to support partial_fit()
        :param poisoning_points: the data points to be used for poisoning
        :param target_class: the target class that the data point needs to obtain in the altered classifier
        :param point_to_hide: the (malicious) data point that should change classification
        :param max_step: the maximal number of step for the attack
        :return: the altered classifier
    """
    predict_init = classifier.predict([point_to_hide])[0]
    predict_current = classifier.predict([point_to_hide])[0]
    step = 0
    while predict_current == predict_init and step < max_step:
        classifier.partial_fit(poisoning_points, [target_class] * len(poisoning_points))
        predict_current = classifier.predict([point_to_hide])[0]
        step += 1
    if step == max_step:
        print("max_step achieved" + str(max_step))
    return classifier
    