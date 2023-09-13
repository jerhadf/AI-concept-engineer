# Conceptual engineering pseudocode

import philosophyExperiments # experimental philosophy methods

def conceptualEngineering(targetConcept):

  identifyConcept(targetConcept)

  diagnoseConcept(targetConcept)

  reverseEngineerConcept(targetConcept)

  makeEthicalAssessment(targetConcept)

  constructNewConceptualization(targetConcept)

  empiricallyEvaluateConcepts(targetConcept)

  refineConcept(targetConcept)

  makeAcceptanceDecision(targetConcept)

  if conceptAccepted:
     advocateForConcept(targetConcept)
  else:
     rejectConcept(targetConcept)

def identifyConcept(concept):
  print("Identifying concept needing improvement: " + concept)

def diagnoseConcept(concept):
  print("Diagnosing issues with concept: " + concept)

  philosophyExperiments.studyConcept(concept)

  issues = philosophyExperiments.getConceptIssues(concept)

def reverseEngineerConcept(concept):
  print("Reverse engineering concept function: " + concept)

  currentFunction = philosophyExperiments.getConceptFunction(concept)

def makeEthicalAssessment(concept):
  print("Ethical assessment of concept function: " + concept)

  shouldChangeFunction = conceptualEthicist.makeEthicalAssessment(currentFunction)

def constructNewConceptualization(concept):
  print("Constructing new conceptualization for: " + concept)

  if shouldChangeFunction:
     targetFunction = conceptualEthicist.proposeNewFunction(concept)
  else:
     targetFunction = currentFunction

  newConcept = conceptualEngineer.constructConcept(concept, targetFunction)

def empiricallyEvaluateConcepts(concept):
  print("Evaluating concepts empirically: " + concept)

  philosophyExperiments.evaluateConcept(concept)
  philosophyExperiments.evaluateConcept(newConcept)

def refineConcept(concept):
  print("Refining concept through iteration: " + concept)

  while philosophyExperiments.conceptNeedsRefining(newConcept):
    newConcept = conceptualEngineer.refineConcept(newConcept)
    philosophyExperiments.evaluateConcept(newConcept)

def makeAcceptanceDecision(concept):
  print("Philosophical and ethical assessment: " + concept)

  conceptAccepted = conceptualEthicist.makeAcceptanceDecision(newConcept)

def advocateForConcept(concept):
  print("Advocating for adoption of concept: " + concept)

  conceptualAdvocate.advocateForConcept(concept)

def rejectConcept(concept):
  print("Concept rejected by ethical assessment: " + concept)

# Example usage:

conceptualEngineering("justice")