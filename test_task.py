import pytest
import task

def test_simple_case():
    start_list = ["Jennifer Figueroa", "Heather Mcgee", "Amanda Schwartz", "Nicole Yoder", "Melissa Hoffman"]
    expected = ["Heather Mcgee", "Nicole Yoder", "Melissa Hoffman", "Jennifer Figueroa", "Amanda Schwartz"]
    assert task.task_1(start_list) == expected

def test_equal_length_surnames():
    start_list = ["John Adams", "Paul Brown", "Jane Black", "Mike Clark"]
    expected = ["Jane Black", "John Adams", "Paul Brown", "Mike Clark"]
    assert task.task_1(start_list) == expected

def test_identical_surnames():
    start_list = ["Anne Smith", "Betty Smith", "Carl Smith"]
    expected = ["Anne Smith", "Betty Smith", "Carl Smith"]
    assert task.task_1(start_list) == expected

def test_single_name():
    start_list = ["Samantha Montgomery"]
    expected = ["Samantha Montgomery"]
    assert task.task_1(start_list) == expected

def test_different_length_surnames():
    start_list = ["Zoe Alpha", "Anna Beta", "John Gamma", "Will Delta"]
    expected = ["Zoe Alpha", "Anna Beta", "John Gamma", "Will Delta"]
    assert task.task_1(start_list) == expected

def test_names_with_hyphenated_surnames():
    start_list = ["Emily Taylor-Smith", "John O'Reilly", "Sarah Johnson"]
    expected = ["Sarah Johnson", "John O'Reilly", "Emily Taylor-Smith"]
    assert task.task_1(start_list) == expected

def test_simple_repeats():
    start_list = ["a", "a", "b", "b", "c", "c", "c"]
    expected = "a2b2c3"
    assert task.task_2(start_list) == expected

def test_single_character():
    start_list = ["a"]
    expected = "a"
    assert task.task_2(start_list) == expected

def test_mixed_repeats_and_singles():
    start_list = ["a", "b", "a", "c", "a", "d", "a", "a"]
    expected = "abacabada2"
    assert task.task_2(start_list) == expected

def test_all_single_characters():
    start_list = ["x", "y", "z"]
    expected = "xyz"
    assert task.task_2(start_list) == expected

def test_longer_repeating_characters():
    start_list = ["m", "m", "m", "m", "n", "o", "o", "o", "p"]
    expected = "m4no3p"
    assert task.task_2(start_list) == expected

def test_alternating_repeats_and_singles():
    start_list = ["p", "q", "q", "r", "r", "r", "s"]
    expected = "pq2r3s"
    assert task.task_2(start_list) == expected

def test_long_single_repeat():
    start_list = ["a"] * 50  # 50 'a's
    expected = "a50"
    assert task.task_2(start_list) == expected

def test_empty_list():
    start_list = []
    expected = ""
    assert task.task_2(start_list) == expected

def test_basic_case():
    staircase = [0, 2, 2, 1]
    expected = 2  # Start at 0, step over the 2nd step, then take step 3 (cost: 0 -> 2 -> 1)
    assert task.task_3(staircase) == expected

def test_two_different_paths_same_cost():
    staircase = [0, 2, 3, 2]
    expected = 3  # Start at 0, step to 2, then step to the end (cost: 0 -> 2 -> 3 -> Top)
    assert task.task_3(staircase) == expected

def test_minimal_cost():
    staircase = [10, 15, 20]
    expected = 15  # Start at step 0 (10), step over 15 to step 20 (cost: 10 -> 15)
    assert task.task_3(staircase) == expected

def test_all_zero_steps():
    staircase = [0, 0, 0, 0, 0, 0]
    expected = 0  # No cost to climb (cost: 0 -> 0 -> 0 -> Top)
    assert task.task_3(staircase) == expected

def test_large_costs():
    staircase = [5, 100, 50, 5, 1, 1, 100]
    expected = 62  # Start at step 0, step 2, step 3, step 4, step 5 (cost: 5 -> 50 -> 5 -> 1 -> 1 -> Top)
    assert task.task_3(staircase) == expected

def test_single_step():
    staircase = [10]
    expected = 10  # Only one step, so cost is 10
    assert task.task_3(staircase) == expected

def test_two_steps():
    staircase = [1, 100]
    expected = 1  # Start on step 1, no need to step on 100 (cost: 1 -> Top)
    assert task.task_3(staircase) == expected

def test_alternating_high_low_cost():
    staircase = [5, 10, 5, 10, 5]
    expected = 15  # Step on all low-cost steps (cost: 5 -> 5 -> 5 -> Top)
    assert task.task_3(staircase) == expected