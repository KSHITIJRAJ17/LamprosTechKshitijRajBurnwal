from collections import defaultdict

def find_course_order(num_courses, prerequisites):
    graph = defaultdict(list)
    visited = [0] * num_courses
    result = []

    # Build the adjacency list
    for prerequisite in prerequisites:
        course, prereq = prerequisite
        graph[prereq].append(course)

    def dfs(course):
        # Mark the current course as visited
        visited[course] = 1

        # Visit all neighbors (prerequisites) of the current course
        for neighbor in graph[course]:
            if visited[neighbor] == 0:
                dfs(neighbor)

        # Add the current course to the result
        result.append(course)

    # Perform DFS for each course
    for course in range(num_courses):
        if visited[course] == 0:
            dfs(course)

    # Reverse the result to get the topological order
    result.reverse()

    # Check if there is a valid course order
    if len(result) == num_courses:
        return result
    else:
        return []

#Running a sample case.
num_courses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
print("List of prerequisites are:",prerequisites)
course_order = find_course_order(num_courses, prerequisites)
if course_order:
    print("Valid Course Order:", course_order)
else:
    print("No valid course order exists.")
