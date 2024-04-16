import pytest
from all_questions import *
import pickle



#-----------------------------------------------------------
def question1():
    answers = {}

    # type: float
    # Calculate the probability.
    answers['(a)'] = 0.028

    # type: float
    # Calculate the probability.
    answers['(b)'] = 0.002

    # type: float
    # Calculate the probability.
    answers['(c)'] = 0.08
    return answers


#-----------------------------------------------------------
def question2():
    answers = {}

    # type: bool
    answers['(a) A'] = True

    # type: bool
    answers['(a) B'] = False

    # type: bool
    answers['(a) C'] = False

    # type: bool
    answers['(a) D'] = True

    # type: bool
    answers['(b) A'] = True

    # type: False
    answers['(b) B'] = False

    # type: bool
    answers['(b) C'] = True

    # type: bool
    answers['(b) D'] = False

    # type: eval_float
    # The formulas should only use the variable 'p'. The formulas should be
    # a valid Python expression. Use the functions in the math module as
    # required.
    answers['(c) Weight update'] = '(1/2)*math.log((1-p)/p)' # the answer is 0.423

    # type: float
    # the answer should be correct to 3 significant digits
    answers['(d) Weight influence'] = 1.527
    return answers


#-----------------------------------------------------------
def question3():
    answers = {}

    # type: string
    answers['Agree?'] = 'no'

    # type: explain_string
    answers['Explain'] = "Because flipping a coin is completely random and has no predictive value, Alan's method is ineffective because it ignores all crucial information on changes in the stock market. Coin flipping is not a random chance; ensemble approaches rely on combining predictions from models that are individually better than chance."
    return answers


#-----------------------------------------------------------
def question4():
    answers = {}

    # type: bool
    answers['(a) e=0.5, independent'] = False

    # type: bool
    answers['(b), independent'] = True

    # type: bool
    answers['(c) identical'] = False
    return answers


#-----------------------------------------------------------
def question5():
    answers = {}

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(a)'] = 'iii'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(b)'] = 'i'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(c)'] = 'ii'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(d)'] = 'iv'
    return answers


#-----------------------------------------------------------
def question6():
    answers = {}

    # type: eval_float
    answers['(a) C1-TPR'] = 'p'

    # type: eval_float
    answers['(a) C2-TPR'] = '2*p'

    # type: eval_float
    answers['(a) C1-FPR'] = 'p'

    # type: eval_float
    answers['(a) C2-FPR'] = '2*p'

    # type: string
    # Hint: The random guess line in an ROC curve corresponds to TPR=FPR.
    # choices: ['yes', 'no']
    answers['(b) C2 better classifier than C1?'] = 'no'

    # type: explain_string
    answers['(b) C2 better classifier than C1? Explain'] = "Since both C2 and C1 fall on the random guess line of a ROC curve, which indicates no predictive power beyond random chance, they are not superior classifiers than C1."

    # type: string
    # choices: ['TPR/FPR', 'precision/recall']
    answers['(c) Which metric?'] = 'precision/recall'

    # type: explain_string
    answers['(c) explain'] = "In this case, precision and recall provide additional information since they take into account the model's capacity to identify all positive samples (recall) and strike a balance between genuine positives and the prediction's relevance (precision). Based on these measures, C2 might be regarded as a superior classifier than C1, as it has a higher recall."
    return answers


#-----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    # choices: ['C1', 'C2', 'None']
    answers['(i) Best classifier?'] = 'C2'

    # type: explain_string
    answers['(i) Best classifier, explain'] = "In this case, precision and recall provide additional information since they take into account the model's capacity to identify all positive samples (recall) and strike a balance between genuine positives and the prediction's relevance (precision). Based on these measures, C2 might be regarded as a superior classifier than C1, as it has a higher recall."

    # type: string
    # choices: ['TPR-FPR', 'precision-recall-F1-Measure']
    answers['(ii) appropriate metric pair'] = 'precision-recall-F1-Measure'

    # type: explain_string
    answers['(ii) appropriate metric pair, explain'] = "The right metrics to use are precision, recall, and F1-measure since they give a more comprehensive picture of a classifier's performance, particularly when the dataset is imbalanced and there are a lot fewer positive cases than negative ones."

    # type: string
    # choices: ['C1', 'C2', 'C3']
    answers['(iii) preferred classifier?'] = 'C2'

    # type: explain_string
    answers['(iii) best classifier, explain'] = "As seen by its greatest F1-measure among the classifiers, C2 is favoured because it preserves a balance between precision and recall. C3, which has the maximum precision, is less ideal in circumstances when identifying all positives is crucial because it does so at the expense of recall."
    return answers


#-----------------------------------------------------------
def question8():
    answers = {}

    # type: eval_float
    answers['(a) precision for C0'] = 'p'

    # type: eval_float
    answers['(a) recall for C0'] = 'p'

    # type: eval_float
    answers['(b) F-measure of C0'] = '2*(0.1*p)/(0.1+p)'

    # type: string
    # choices: ['yes', 'no', 'unknown']
    answers['C1 better than random?'] = 'yes'

    # type: float
    # What is the range of p for which C1 is better than random?  What is
    # "?" in the expression "p > ?"

    answers['p-range'] = 0.3
    return answers


#-----------------------------------------------------------
def question9():
    answers = {}

    # type: dict[string,float]
    # keys: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) metrics'] = {'precision':0.61538, 'recall':5.3333, 'F-measure': 0.5714, 'accuracy':0.88}

    # type: string
    # choices: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) best metric?'] = 'F-measure'

    # type: string
    # choices: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) worst metric?'] = 'accuracy'

    # type: explain_string
    answers['(ii) Explain your choices of best and worst metrics'] = "The F-measure is the most appropriate metric in this situation because it strikes a compromise between precision and recall, which is critical in situations involving imbalanced classes, like weather prediction, where one result may be noticeably more prevalent than the other. The poorest statistic is accuracy since it can be abnormally high because of a high number of true negatives, which does not always mean that the minority class is performing well in terms of prediction."
    return answers


#-----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    # choices: ['T1', 'T2']
    answers['(a) better test based on F-measure?'] = 'T1'

    # type: string
    # choices: ['T1', 'T2']
    answers['(b) better test based on TPR/FPR?'] = 'T2'

    # type: string
    # choices: ['F1', 'TPR/FPR']
    answers['(c) Which evaluation measure to use between the two tests?'] = 'TPR/FPR'

    # type: explain_string
    answers['(c) Which evaluation measure? Explain'] = "TPR/FPR is the most appropriate metric for assessing cancer detection tests T1 and T2, highlighting the significance of the test's capacity to accurately identify true positives when the substantial cost of failing to detect a diagnosis (false negative) exceeds the hazards of false positives in a medical perspective."

    # type: explain_string
    answers['(d) Example scenario where you would reverse choise in (c)'] = "In scenarios where the disease is rare and the cost of false positives is high, you might prioritize the TPR/FPR ratio. For example, in large-scale screenings for a rare condition, a high number of false positives could overwhelm the healthcare system with unnecessary follow-up procedures. In this case, a higher TPR/FPR ratio indicates a more efficient test, reducing the burden of false positives while still identifying those truly affected."
    return answers
#-----------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
