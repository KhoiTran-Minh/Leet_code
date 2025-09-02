import heapq

class Solution:
    def maxAverageRatio(self, classes, extraStudents):
        # Max-heap to store classes and their potential gains
        max_heap = []
        
        # Initialize the heap with the current pass ratio and the potential gain
        for pass_i, total_i in classes:
            # Ensure we are using floating-point division
            gain = (float(pass_i + 1) / (total_i + 1)) - (float(pass_i) / total_i)
            # Use negative gain to simulate a max-heap (heapq is a min-heap by default)
            heapq.heappush(max_heap, (-gain, pass_i, total_i))
        
        # Assign the extra students
        for _ in range(extraStudents):
            # Extract the class with the maximum gain
            neg_gain, pass_i, total_i = heapq.heappop(max_heap)
            
            # Update the pass and total students for this class
            pass_i += 1
            total_i += 1
            
            # Recalculate the new gain for this class after adding an extra student
            new_gain = (float(pass_i + 1) / (total_i + 1)) - (float(pass_i) / total_i)
            
            # Push the updated class back to the heap with the new gain
            heapq.heappush(max_heap, (-new_gain, pass_i, total_i))
        
        # Calculate the final average pass ratio
        total_ratio = 0
        for _, pass_i, total_i in max_heap:
            total_ratio += pass_i / total_i
        
        # Return the average ratio, rounded to 5 decimal places
        return round(total_ratio / len(classes), 5)

