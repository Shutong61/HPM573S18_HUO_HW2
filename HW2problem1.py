#  Implement the HUI3 instrument

Constant = 1.371
N = 0.371

dicAttributes = {'Vision': [1.00, 0.98, 0.89, 0.84, 0.75, 0.61],
                 'Hearing': [1.00, 0.95, 0.89, 0.80, 0.74, 0.61],
                 'Speech': [1.00, 0.94, 0.89, 0.81, 0.68],
                 'Ambulation': [1.00, 0.93, 0.86, 0.73, 0.65, 0.58],
                 'Dexterity': [1.00, 0.95, 0.88, 0.76, 0.65, 0.56],
                 'Emotion': [1.00, 0.95, 0.85, 0.64, 0.46],
                 'Cognition': [1.00, 0.92, 0.95, 0.83, 0.60,0.42],
                 'Pain': [1.00, 0.96, 0.90, 0.77, 0.55]}; # 8 attributes in HUI3 instrument

def get_score(vision, hearing, speech, ambulation, dexterity, emotion, cognition,pain):
    """

    :param vision:
    :param hearing:
    :param speech:
    :param ambulation:
    :param dexterity:
    :param emotion:
    :param cognition:
    :param pain:
    :return:
    """

    if not (vision in [1, 2, 3, 4, 5, 6]):
        raise ValueError('Vision level can take only 1, 2, 3, 4, 5 or 6')
    if not (hearing in [1, 2, 3, 4, 5, 6]):
        raise ValueError('Hearing level can take only 1, 2, 3, 4, 5 or 6')
    if not (speech in [1, 2, 3, 4, 5]):
        raise ValueError('Speech level can take only 1, 2, 3, 4 or 5')
    if not (ambulation in [1, 2, 3, 4, 5, 6]):
        raise ValueError('Ambulation level can take only 1, 2, 3, 4, 5 or 6')
    if not (dexterity in [1, 2, 3, 4, 5, 6]):
        raise ValueError('Dexterity level can take only 1, 2, 3, 4, 5 or 6')
    if not (emotion in [1, 2, 3, 4, 5]):
        raise ValueError('Emotion level can take only 1, 2, 3, 4 or 5')
    if not (cognition in [1, 2, 3, 4, 5, 6]):
        raise ValueError('Cognition level can take only 1, 2, 3, 4, 5 or 6')
    if not (pain in [1, 2, 3, 4, 5]):
        raise ValueError('Pain level can take only 1, 2, 3, 4 or 5')

    score = Constant

    score *= dicAttributes['Vision'][vision -1]
    score *= dicAttributes['Hearing'][hearing - 1]
    score *= dicAttributes['Speech'][speech -1]
    score *= dicAttributes['Ambulation'][ambulation - 1]
    score *= dicAttributes['Dexterity'][dexterity -1]
    score *= dicAttributes['Emotion'][emotion - 1]
    score *= dicAttributes['Cognition'][cognition - 1]
    score *= dicAttributes['Pain'][pain - 1]
    score -= N

    return score





