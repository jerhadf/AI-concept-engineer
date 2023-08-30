import philosophyExperiments

def conceptualEngineering(target_concept):
  """
  Main process for conceptual engineering.

  Args:
    target_concept (str): The concept to engineer

  Steps:
    1. Identify concept needing improvement
    2. Diagnose issues with concept
    3. Reverse engineer concept to determine function
    4. Make ethical assessment of concept function
    5. Construct new conceptualization
    6. Empirically evaluate concepts
    7. Refine concept through iteration
    8. Make acceptance decision
    9. Advocate for accepted concept
  """

  identify_concept(target_concept)

  diagnose_concept(target_concept)

  reverse_engineer_concept(target_concept)

  make_ethical_assessment(target_concept)

  new_concept = construct_new_conceptualization(target_concept)

  evaluate_concepts(target_concept, new_concept)

  refine_concept(new_concept)

  if make_acceptance_decision(new_concept):
     advocate_for_concept(new_concept)
  else:
     reject_concept(new_concept)


def identify_concept(concept):
  """
  Identify a concept in need of improvement.

  Look for concepts that are unclear, confused, or defective based on issues like:
    - Intuition clashes/inconsistencies involving concept
    - Concept obscures distinctions that should be made
    - Meaning of concept is especially unclear or confusing
  """
  print(f"Identifying concept needing improvement: {concept}")


def diagnose_concept(concept):
  """
  Diagnose issues with the identified concept.

  Study the concept empirically using experimental philosophy methods to reveal
  problems and deficiencies. Issues may include:
    - Reliance on defective or unreliable intuitions
    - Sensitivity to irrelevant factors
    - Lack of explanatory power
    - Vagueness or unclarity
  """
  print(f"Diagnosing issues with concept: {concept}")

  # Use experimental philosophy to study concept
  philosophyExperiments.study_concept(concept)

  # Identify issues
  issues = philosophyExperiments.get_concept_issues(concept)


def reverse_engineer_concept(concept):
  """
  Reverse engineer the concept to determine its current function.

  Examine current and historical usage of the concept to identify its purpose,
  i.e. what it allows us to do. Can use methods like:
    - Studying current patterns of use
    - Considering historical development and introduction of concept
    - Identifying paradigmatic examples and uses
  """
  print(f"Reverse engineering concept function: {concept}")

  function = philosophyExperiments.get_concept_function(concept)


def make_ethical_assessment(concept):
  """
  Make an ethical assessment of the concept's current function.

  Evaluate whether the current function is acceptable or should be changed
  based on moral, epistemic, and prudential factors.

  Returns:
    True if function should be changed, False otherwise.
  """
  print(f"Making ethical assessment of concept function: {concept}")

  change_needed = conceptualEthicist.make_ethical_assessment(function)
  return change_needed


def construct_new_conceptualization(concept):
  """
  Construct a new conceptualization if needed.

  If ethical assessment determined the function should change, construct a new
  concept with an improved function. Otherwise, keep the original concept.

  Returns:
    The new engineered concept
  """

  print(f"Constructing new conceptualization for: {concept}")

  if make_ethical_assessment(concept):
    new_function = conceptualEthicist.propose_new_function(concept)
  else:
    new_function = function

  return conceptualEngineer.construct_concept(concept, new_function)


def evaluate_concepts(original_concept, new_concept):
  """
  Empirically evaluate the function of both the original and engineered concepts.

  This allows comparing to determine if the new concept is an improvement over
  the original.

  Args:
    original_concept: The pre-engineering concept
    new_concept: The engineered concept
  """

  print("Evaluating concepts empirically")

  philosophyExperiments.evaluate_concept(original_concept)
  philosophyExperiments.evaluate_concept(new_concept)


def refine_concept(concept):
  """
  Iterate testing and refinement until the engineered concept is satisfactory.
  """

  print(f"Refining concept through iteration: {concept}")

  while philosophyExperiments.concept_needs_refining(concept):
    improved_concept = conceptualEngineer.refine_concept(concept)
    evaluate_concepts(concept, improved_concept)
    concept = improved_concept


def make_acceptance_decision(concept):
  """
  Make a philosophical and ethical assessment to determine whether to accept
  or reject the engineered concept.

  Returns:
    True if concept is accepted, False if rejected
  """

  print(f"Making acceptance decision: {concept}")

  return conceptualEthicist.make_acceptance_decision(concept)


def advocate_for_concept(concept):
  """
  Advocate for the adoption and implementation of an accepted concept.
  """

  print(f"Advocating for concept adoption: {concept}")

  conceptualAdvocate.advocate_for_concept(concept)


def reject_concept(concept):
  """
  Reject a concept that failed acceptance.
  """

  print(f"Concept rejected: {concept}")