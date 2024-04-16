#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>

#define MAX_PAGE_REQUESTS 2000
#define PAGE_NUMBER_RANGE 513

// Function declarations for the page replacement algorithms and utilities
void fifo(int frames, int pageRequests[], int n);
void lru(int frames, int pageRequests[], int n);
void opt(int frames, int pageRequests[], int n);
void clock_replacement(int frames, int pageRequests[], int n);
void print_snapshot(int frames, int pageRequests[], int snapshotIndex, int *currentFrame);

int main() {
    int pageRequests[MAX_PAGE_REQUESTS];
    int frames, snapshotIndex;

    // Seed the random number generator
    srand(time(NULL));

    // Generate a random page request stream
    for (int i = 0; i < MAX_PAGE_REQUESTS; i++) {
        pageRequests[i] = rand() % PAGE_NUMBER_RANGE;
    }

    // Get the number of frames from the user
    printf("Enter the frames allowed: ");
    scanf("%d", &frames);

    // Simulate page replacement algorithms
    printf("Frame Size - %d\n\nAlgos PF Rate\n", frames);
    fifo(frames, pageRequests, MAX_PAGE_REQUESTS);
    lru(frames, pageRequests, MAX_PAGE_REQUESTS);
    opt(frames, pageRequests, MAX_PAGE_REQUESTS);
    clock_replacement(frames, pageRequests, MAX_PAGE_REQUESTS);

    // Snapshot viewer interaction
    do {
        printf("\nWhich frame snapshot to be displayed (-1 to exit): ");
        scanf("%d", &snapshotIndex);
        if (snapshotIndex == -1) {
            break;
        }
        print_snapshot(frames, pageRequests, snapshotIndex, NULL); // Passing NULL for simplicity
    } while (true);

    return 0;
}

void fifo(int frames, int pageRequests[], int n) {
    int pageFaults = 0;
    int frameBuffer[frames];
    int insertPos = 0;

    // Initialize the frame buffer
    for (int i = 0; i < frames; i++) {
        frameBuffer[i] = -1;
    }

    // Simulate the FIFO page replacement
    for (int i = 0; i < n; i++) {
        bool found = false;
        for (int j = 0; j < frames; j++) {
            if (frameBuffer[j] == pageRequests[i]) {
                found = true;
                break;
            }
        }
        if (!found) {
            frameBuffer[insertPos] = pageRequests[i];
            insertPos = (insertPos + 1) % frames;
            pageFaults++;
        }
    }

    printf("FIFO %.4f\n", (float)pageFaults / n);
}

void lru(int frames, int pageRequests[], int n) {
    int pageFaults = 0;
    int frameBuffer[frames];
    int lastUsed[frames];

    // Initialize the frame buffer and last used times
    for (int i = 0; i < frames; i++) {
        frameBuffer[i] = -1;
        lastUsed[i] = -1;
    }

    // Simulate the LRU page replacement
    for (int i = 0; i < n; i++) {
        int leastRecentlyUsed = i;
        int replacePos = -1;
        bool found = false;

        for (int j = 0; j < frames; j++) {
            if (frameBuffer[j] == pageRequests[i]) {
                found = true;
                lastUsed[j] = i;
                break;
            }
            if (lastUsed[j] < leastRecentlyUsed) {
                leastRecentlyUsed = lastUsed[j];
                replacePos = j;
            }
        }

        if (!found) {
            if (replacePos == -1) replacePos = 0; // For the initial case when all frames are -1
            frameBuffer[replacePos] = pageRequests[i];
            lastUsed[replacePos] = i;
            pageFaults++;
        }
    }

    printf("LRU %.4f\n", (float)pageFaults / n);
}

void opt(int frames, int pageRequests[], int n) {
    int pageFaults = 0;
    int frameBuffer[frames];

    // Initialize the frame buffer
    for (int i = 0; i < frames; i++) {
        frameBuffer[i] = -1;
    }

    // Simulate the OPT page replacement
    for (int i = 0; i < n; i++) {
        bool found = false;
        for (int j = 0; j < frames; j++) {
            if (frameBuffer[j] == pageRequests[i]) {
                found = true;
                break;
            }
        }

        if (!found) {
            int farthest = i, replacePos = -1;
            for (int j = 0; j < frames; j++) {
                int nextUse = n;
                for (int k = i + 1; k < n; k++) {
                    if (frameBuffer[j] == pageRequests[k]) {
                        nextUse = k;
                        break;
                    }
                }
                if (nextUse > farthest) {
                    farthest = nextUse;
                    replacePos = j;
                }
            }
            if (replacePos == -1) replacePos = 0; // For the initial case when all frames are -1
            frameBuffer[replacePos] = pageRequests[i];
            pageFaults++;
        }
    }

    printf("OPT %.4f\n", (float)pageFaults / n);
}

void clock_replacement(int frames, int pageRequests[], int n) {
    int pageFaults = 0;
    int frameBuffer[frames];
    bool referenceBit[frames];
    int pointer = 0;

    // Initialize frame buffer and reference bits
    for (int i = 0; i < frames; i++) {
        frameBuffer[i] = -1;
        referenceBit[i] = false;
    }

    // Simulate the CLOCK page replacement
    for (int i = 0; i < n; i++) {
        bool found = false;
        while (!found) {
            for (int j = 0; j < frames; j++) {
                int index = (pointer + j) % frames;
                if (frameBuffer[index] == pageRequests[i]) {
                    referenceBit[index] = true;
                    found = true;
                    break;
                }
            }
            if (!found) {
                while (referenceBit[pointer]) {
                    referenceBit[pointer] = false;
                    pointer = (pointer + 1) % frames;
                }
                frameBuffer[pointer] = pageRequests[i];
                referenceBit[pointer] = true;
                pointer = (pointer + 1) % frames;
                pageFaults++;
            }
        }
    }

    printf("CLOCK %.4f\n", (float)pageFaults / n);
}

void print_snapshot(int frames, int pageRequests[], int snapshotIndex, int *currentFrame) {
    printf("** Print the page stream request here **\n");
    int start = snapshotIndex - 10 >= 0 ? snapshotIndex - 10 : 0;
    int end = snapshotIndex + 10 < MAX_PAGE_REQUESTS ? snapshotIndex + 10 : MAX_PAGE_REQUESTS - 1;

    for (int i = start; i <= end; i++) {
        printf("%d ", pageRequests[i]);
    }
    printf("\n");
}
