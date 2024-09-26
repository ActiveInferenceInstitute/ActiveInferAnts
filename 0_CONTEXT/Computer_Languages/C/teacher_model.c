#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define MAX_STATES 100

typedef struct {
    double knowledge[MAX_STATES];
    int n_states;
} Teacher;

void init_teacher(Teacher* teacher, int n_states) {
    teacher->n_states = n_states;
    for (int i = 0; i < n_states; i++) {
        teacher->knowledge[i] = 0.0;
    }
}

void update_teacher_knowledge(Teacher* teacher, int state) {
    if (state >= 0 && state < teacher->n_states) {
        // Logistic growth model for teacher's knowledge
        double current_knowledge = teacher->knowledge[state];
        double growth_rate = 0.1;
        double max_knowledge = 1.0;
        
        teacher->knowledge[state] = (max_knowledge * current_knowledge * exp(growth_rate)) / 
                                    (max_knowledge + current_knowledge * (exp(growth_rate) - 1));
    }
}

double* get_teacher_knowledge(Teacher* teacher) {
    return teacher->knowledge;
}

// Helper function to find the index of the maximum value in an array
int argmax(double* arr, int n) {
    int max_idx = 0;
    for (int i = 1; i < n; i++) {
        if (arr[i] > arr[max_idx]) {
            max_idx = i;
        }
    }
    return max_idx;
}

int suggest_resource(Teacher* teacher, double* student_beliefs) {
    double knowledge_gaps[MAX_STATES];
    for (int i = 0; i < teacher->n_states; i++) {
        knowledge_gaps[i] = (1.0 - teacher->knowledge[i]) * student_beliefs[i];
    }
    return argmax(knowledge_gaps, teacher->n_states);
}