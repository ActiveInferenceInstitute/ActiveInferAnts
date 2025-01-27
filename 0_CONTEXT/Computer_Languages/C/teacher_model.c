#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define MAX_STATES 100

typedef struct {
    double* knowledge;  // Dynamic array
    double growth_rate;
    double max_knowledge;
    int n_states;
} Teacher;

typedef enum {
    TEACHER_OK,
    TEACHER_INVALID_INPUT,
    TEACHER_MEMORY_ERROR,
    TEACHER_STATE_MISMATCH,
    TEACHER_NOT_INITIALIZED
} TeacherError;

const char* teacher_error_string(TeacherError err) {
    static const char* strings[] = {
        "Success",
        "Invalid input parameters",
        "Memory allocation failed",
        "State dimension mismatch",
        "Teacher not initialized properly"
    };
    return (err >= 0 && err <= TEACHER_NOT_INITIALIZED) ? strings[err] : "Unknown error";
}

// Add initialization check macro
#define TEACHER_CHECK(t) do { \
    if (!(t) || !(t)->knowledge || (t)->n_states <= 0) \
        return TEACHER_NOT_INITIALIZED; \
} while(0)

int init_teacher(Teacher* teacher, int n_states, double growth_rate, double max_knowledge) {
    if (n_states <= 0 || n_states > MAX_STATES) return -1;
    if (growth_rate <= 0.0) return -1;
    
    teacher->n_states = n_states;
    teacher->growth_rate = growth_rate;
    teacher->max_knowledge = max_knowledge;
    
    teacher->knowledge = (double*)malloc(n_states * sizeof(double));
    if (!teacher->knowledge) return -1;
    
    for (int i = 0; i < n_states; i++) {
        teacher->knowledge[i] = 0.0;
    }
    return 0;
}

void update_teacher_knowledge(Teacher* teacher, int state) {
    if (!teacher || state < 0 || state >= teacher->n_states) return;
    
    // Use struct parameters instead of hard-coded values
    double current = teacher->knowledge[state];
    double exp_gr = exp(teacher->growth_rate);
    
    teacher->knowledge[state] = (teacher->max_knowledge * current * exp_gr) /
                               (teacher->max_knowledge + current * (exp_gr - 1));
}

/**
 * @brief Gets copy of teacher's knowledge state
 * @param teacher Teacher instance
 * @param buffer Output buffer (size must match n_states)
 * @return 0 on success, -1 on error
 */
int get_teacher_knowledge(const Teacher* teacher, double* buffer, int buffer_size) {
    if (!teacher || !buffer || buffer_size != teacher->n_states) return -1;
    
    memcpy(buffer, teacher->knowledge, teacher->n_states * sizeof(double));
    return 0;
}

/**
 * @brief Finds index of maximum value in array with safety checks
 * @param arr Array to search
 * @param n Number of elements in array
 * @return Index of maximum value, -1 for invalid input
 */
static int argmax(const double* arr, int n) {
    if (!arr || n <= 0) return -1;
    
    int max_idx = 0;
    for (int i = 1; i < n; i++) {
        if (arr[i] > arr[max_idx]) {
            max_idx = i;
        }
    }
    return max_idx;
}

int suggest_resource(const Teacher* teacher, const double* student_beliefs, int student_n_states) {
    if (!teacher || !student_beliefs || teacher->n_states != student_n_states) return -1;
    
    double* gaps = (double*)malloc(teacher->n_states * sizeof(double));
    if (!gaps) return -1;
    
    for (int i = 0; i < teacher->n_states; i++) {
        gaps[i] = (teacher->max_knowledge - teacher->knowledge[i]) * student_beliefs[i];
    }
    
    int result = argmax(gaps, teacher->n_states);
    free(gaps);
    return result;
}

// Add destruction function for memory management
void destroy_teacher(Teacher* teacher) {
    if (teacher) {
        free(teacher->knowledge);
        teacher->knowledge = NULL;
        teacher->n_states = 0;
    }
}

typedef struct {
    Teacher* (*compose)(const Teacher* t1, const Teacher* t2);
    Teacher* (*product)(const Teacher* t1, const Teacher* t2);
    Teacher* (*coproduct)(const Teacher* t1, const Teacher* t2);
} TeacherOperations;

TeacherError teacher_compose(Teacher* dest, const Teacher* t1, const Teacher* t2) {
    TEACHER_CHECK(t1);
    TEACHER_CHECK(t2);
    if (!dest) return TEACHER_INVALID_INPUT;
    
    // Implement knowledge composition using component-wise geometric mean
    for (int i = 0; i < dest->n_states; i++) {
        dest->knowledge[i] = sqrt(t1->knowledge[i] * t2->knowledge[i]);
    }
    return TEACHER_OK;
}

TeacherError teacher_product(Teacher* dest, const Teacher* t1, const Teacher* t2) {
    TEACHER_CHECK(t1);
    TEACHER_CHECK(t2);
    if (!dest || dest->n_states != t1->n_states + t2->n_states)
        return TEACHER_STATE_MISMATCH;
    
    // Concatenate knowledge states
    memcpy(dest->knowledge, t1->knowledge, t1->n_states * sizeof(double));
    memcpy(dest->knowledge + t1->n_states, t2->knowledge, t2->n_states * sizeof(double));
    return TEACHER_OK;
}

TeacherError teacher_serialize(const Teacher* teacher, const char* filename) {
    TEACHER_CHECK(teacher);
    if (!filename) return TEACHER_INVALID_INPUT;
    
    FILE* fp = fopen(filename, "wb");
    if (!fp) return TEACHER_INVALID_INPUT;
    
    size_t written = 0;
    written += fwrite(&teacher->n_states, sizeof(int), 1, fp);
    written += fwrite(&teacher->growth_rate, sizeof(double), 1, fp);
    written += fwrite(&teacher->max_knowledge, sizeof(double), 1, fp);
    written += fwrite(teacher->knowledge, sizeof(double), teacher->n_states, fp);
    
    fclose(fp);
    return (written == 2 + teacher->n_states) ? TEACHER_OK : TEACHER_INVALID_INPUT;
}

TeacherError teacher_deserialize(Teacher* teacher, const char* filename) {
    if (!teacher || !filename) return TEACHER_INVALID_INPUT;
    
    FILE* fp = fopen(filename, "rb");
    if (!fp) return TEACHER_INVALID_INPUT;
    
    int n_states;
    double growth_rate, max_knowledge;
    
    if (fread(&n_states, sizeof(int), 1, fp) != 1 ||
        fread(&growth_rate, sizeof(double), 1, fp) != 1 ||
        fread(&max_knowledge, sizeof(double), 1, fp) != 1) {
        fclose(fp);
        return TEACHER_INVALID_INPUT;
    }
    
    TeacherError err = init_teacher(teacher, n_states, growth_rate, max_knowledge);
    if (err != TEACHER_OK) {
        fclose(fp);
        return err;
    }
    
    if (fread(teacher->knowledge, sizeof(double), n_states, fp) != n_states) {
        destroy_teacher(teacher);
        fclose(fp);
        return TEACHER_INVALID_INPUT;
    }
    
    fclose(fp);
    return TEACHER_OK;
}