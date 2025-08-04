# NLP Use: Prevent division errors in accuracy/precision calculation

true_positives = 50
false_positives = 0
try:
    precision = true_positives/(true_positives+false_positives)
except ZeroDivisionError:
    print("⚠️ Division by zero while calculating precision.")
    