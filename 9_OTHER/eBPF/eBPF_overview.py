"""
eBPF (extended Berkeley Packet Filter) Overview

eBPF is a revolutionary technology in the Linux kernel that enables safe and efficient execution of user-defined programs in kernel space. It's an evolution of the original Berkeley Packet Filter (BPF) and provides a powerful way to extend kernel functionality without modifying kernel source code or loading kernel modules.

1. Core Concepts:

   a. In-Kernel Virtual Machine:
      - eBPF programs run on a register-based virtual machine within the kernel.
      - Just-in-time (JIT) compilation ensures near-native performance.
      - The VM provides a restricted instruction set for safety and efficiency.
      - Programs are verified before execution to ensure kernel integrity.

   b. Safety and Verification:
      - Strict verification process before execution prevents kernel crashes or compromises.
      - Checks include loop detection, stack bounds checking, and pointer safety.
      - Verifier ensures programs terminate and don't access unauthorized memory.
      - Static analysis techniques are employed to guarantee program correctness.

   c. Maps:
      - Efficient key-value stores for data sharing between eBPF programs and user space.
      - Types include hash maps, arrays, ring buffers, LRU (Least Recently Used) maps, and more.
      - Enable stateful operations and data aggregation across multiple eBPF program invocations.
      - Concurrent access is supported with appropriate locking mechanisms.

   d. Helper Functions:
      - Predefined kernel functions that eBPF programs can call.
      - Provide controlled access to kernel functionality and data structures.
      - Constantly evolving set of helpers to expand eBPF capabilities.
      - Categorized by functionality (e.g., networking, tracing, security).

   e. Program Types:
      - Networking: XDP (eXpress Data Path), TC (Traffic Control), socket operations
      - Tracing and Profiling: kprobes, uprobes, tracepoints, perf events
      - Security: seccomp, LSM (Linux Security Modules)
      - Observability and Monitoring: various kernel and user-space hooks
      - Cgroup: resource control and monitoring for containerized environments

2. Advanced Features:

   a. CO-RE (Compile Once - Run Everywhere):
      - Enables eBPF program portability across different kernel versions.
      - Uses BTF (BPF Type Format) for rich type information.
      - Reduces the need for kernel-specific adjustments in eBPF programs.
      - Simplifies deployment and maintenance of eBPF-based solutions.

   b. BPF Type Format (BTF):
      - Provides detailed type information for eBPF programs and maps.
      - Enhances debugging capabilities and enables CO-RE.
      - Allows for more sophisticated static analysis and verification.
      - Supports advanced features like kernel structure access.

   c. Tail Calls:
      - Allow one eBPF program to call another, enabling modular designs.
      - Useful for implementing complex logic and control flow.
      - Limited to a maximum chain of 33 calls for safety.

   d. BPF-to-BPF Function Calls:
      - Support for calling functions within eBPF programs, improving code reuse.
      - Enables more structured and maintainable eBPF programs.
      - Subject to inlining optimizations by the JIT compiler.

   e. Global Variables:
      - Shared memory between different eBPF program invocations.
      - Useful for maintaining state across multiple events.
      - Subject to atomic operations for thread-safe access.

   f. Bounded Loops:
      - Recent kernel versions support bounded loops in eBPF programs.
      - Enhances expressiveness while maintaining safety guarantees.
      - Requires explicit bounds that can be verified statically.

3. Programming and Development:

   a. Language and Compilation:
      - eBPF programs are typically written in restricted C.
      - Compiled to eBPF bytecode using LLVM/Clang with specific target flags.
      - Recent developments allow for use of Rust and Go for eBPF development.
      - Specialized eBPF-focused languages like bpftrace for rapid prototyping.

   b. Development Frameworks:
      - bcc (BPF Compiler Collection): Python/Lua front-end for eBPF
        * Provides high-level abstractions for common eBPF use cases
        * Includes a rich set of tools and examples
      - libbpf: C library for working with eBPF programs
        * Low-level API for loading and interacting with eBPF programs
        * Supports CO-RE and advanced eBPF features
      - bpftrace: High-level tracing language for eBPF
        * Designed for one-liners and short scripts
        * Powerful syntax for common tracing and monitoring tasks
      - cilium/ebpf: Go library for eBPF development
        * Enables eBPF programming in Go
        * Provides abstractions for common eBPF operations

   c. Tools:
      - bpftool: Utility for inspection and simple manipulation of eBPF objects
        * Can load, dump, and manage eBPF programs and maps
        * Supports BTF and CO-RE features
      - perf: Performance analysis tool with eBPF capabilities
        * Integrates eBPF for advanced performance analysis
        * Supports custom eBPF programs for data collection
      - BPF Compiler Collection (BCC) tools:
        * Large collection of ready-to-use eBPF-based tools
        * Covers various aspects of system observability and networking

4. Use Cases and Applications:

   a. Networking:
      - Packet filtering and manipulation at various points in the network stack
      - Load balancing and traffic shaping with fine-grained control
      - DDoS mitigation through early packet dropping and rate limiting
      - Network security enforcement, including microsegmentation
      - Custom protocol parsing and optimization
      - Network function virtualization (NFV) acceleration

   b. Observability and Monitoring:
      - Performance analysis and tracing of kernel and user-space functions
      - Resource usage monitoring with minimal overhead
      - Distributed tracing in microservices architectures
      - Custom metrics collection and aggregation
      - Real-time system behavior analysis
      - Anomaly detection and performance debugging

   c. Security:
      - Runtime security monitoring and enforcement
      - Sandboxing applications with fine-grained syscall filtering
      - Implementing custom security policies at kernel level
      - Intrusion detection and prevention systems
      - Container security and isolation enforcement
      - Audit logging and forensics data collection

   d. Performance Optimization:
      - Identifying bottlenecks in system calls and application code
      - Optimizing I/O operations and resource utilization
      - Custom caching mechanisms and data path optimizations
      - Adaptive performance tuning based on runtime data
      - Profiling and hot spot analysis with minimal overhead

5. Integration with Kernel Subsystems:

   a. Networking Stack:
      - XDP for high-performance packet processing at the NIC level
        * Allows packet dropping, modification, or redirection before SKB allocation
        * Enables use cases like DDoS mitigation and load balancing
      - TC (Traffic Control) for fine-grained traffic shaping and manipulation
        * Operates on socket buffers (SKBs) for more complex processing
        * Supports various classifier and action combinations

   b. Tracing Infrastructure:
      - kprobes for dynamic kernel function tracing
        * Allows attaching eBPF programs to nearly any kernel function
      - uprobes for user-space function tracing
        * Enables tracing of specific functions in user applications
      - tracepoints for predefined kernel trace events
        * Stable ABI for tracing key kernel events
      - USDT (User Statically-Defined Tracing) for application-specific tracing points

   c. Security Modules:
      - LSM (Linux Security Module) hooks for implementing security policies
        * Allows for custom mandatory access control (MAC) implementations
      - seccomp for syscall filtering and sandboxing
        * Fine-grained control over allowed system calls for applications

   d. Cgroup (Control Groups):
      - Resource control and monitoring for containerized environments
      - Custom accounting and limiting of resources like CPU, memory, and I/O

   e. Filesystem and Block I/O:
      - Tracing and optimizing filesystem operations
      - Custom I/O schedulers and caching mechanisms

6. Performance Characteristics:

   a. Low Overhead:
      - JIT compilation provides near-native performance for eBPF programs
      - Minimal impact on system resources for tracing and monitoring
      - Efficient context switching between kernel and eBPF programs

   b. High Throughput:
      - Capable of processing millions of events per second
      - Efficient for high-speed networking applications, including 100Gbps+ networks
      - Optimized data paths for minimal latency in critical code paths

   c. Scalability:
      - Designed to work efficiently on systems with many cores
      - Can leverage multi-core architectures for parallel processing
      - Efficient use of hardware resources through careful design

7. Limitations and Considerations:

   a. Restricted Programming Model:
      - Limited instruction set compared to full kernel modules
      - Loops must be bounded and verifiable
      - Limited stack size (512 bytes by default)
      - Restricted access to kernel functions and data structures

   b. Kernel Version Dependencies:
      - Some features require recent kernel versions
      - CO-RE helps mitigate version-specific issues, but not all features are supported
      - Backwards compatibility considerations for widely deployed systems

   c. Learning Curve:
      - Requires understanding of kernel internals and eBPF concepts
      - Debugging can be challenging due to in-kernel execution
      - Evolving ecosystem with frequent updates and new features

   d. Tooling and Development Environment:
      - Specialized tools and compilers required for development
      - Integration with existing debugging and profiling tools can be complex
      - Continuous adaptation needed to keep up with kernel changes

8. Future Directions:

   a. Expanded Use in Cloud Native Environments:
      - Growing adoption in Kubernetes and container ecosystems
      - Enhanced networking and security features for microservices architectures
      - Integration with service mesh and API gateway technologies

   b. Hardware Offloading:
      - Potential for offloading eBPF programs to smart NICs and DPUs
      - Exploration of eBPF-like programs on other architectures (e.g., ARM, RISC-V)
      - Closer integration with hardware acceleration features

   c. Continued Feature Expansion:
      - Ongoing work to increase eBPF capabilities and use cases
      - Potential for user-space eBPF runtime for enhanced portability
      - Exploration of eBPF use in other operating systems (e.g., Windows, macOS)

   d. Standardization and Ecosystem Growth:
      - Efforts towards standardizing eBPF across different platforms
      - Expansion of development tools and frameworks
      - Growing community and commercial adoption driving innovation

eBPF has fundamentally changed Linux kernel programmability, offering a safe, efficient, and dynamic way to extend kernel functionality. Its impact spans networking, security, and observability domains, making it a crucial technology for modern Linux systems and cloud-native environments. As eBPF continues to evolve, it promises to unlock even more powerful capabilities for system programmers and administrators, enabling unprecedented levels of customization, optimization, and insight into system behavior.
"""

# Example: Advanced eBPF program using libbpf-python to trace process executions with additional context

from bcc import BPF
import ctypes as ct
import time

# eBPF program written in C
bpf_program = """
#include <uapi/linux/ptrace.h>
#include <linux/sched.h>
#include <linux/fs.h>

struct data_t {
    u32 pid;
    u32 ppid;
    u64 start_time;
    char comm[TASK_COMM_LEN];
    char filename[DNAME_INLINE_LEN];
};

BPF_PERF_OUTPUT(events);
BPF_HASH(start, u32, u64);

TRACEPOINT_PROBE(sched, sched_process_exec) {
    struct data_t data = {};
    
    // Get process ID and parent process ID
    data.pid = bpf_get_current_pid_tgid() >> 32;
    data.ppid = (bpf_get_current_task())->real_parent->tgid;
    
    // Get process name
    bpf_get_current_comm(&data.comm, sizeof(data.comm));
    
    // Get start time
    u64 ts = bpf_ktime_get_ns();
    start.update(&data.pid, &ts);
    
    // Get filename of the executed program
    struct file *file = (struct file *)args->filename;
    bpf_probe_read_kernel(&data.filename, sizeof(data.filename), file->f_path.dentry->d_name.name);
    
    events.perf_submit(args, &data, sizeof(data));
    return 0;
}

TRACEPOINT_PROBE(sched, sched_process_exit) {
    u32 pid = bpf_get_current_pid_tgid() >> 32;
    u64 *start_ts = start.lookup(&pid);
    if (start_ts) {
        u64 duration = bpf_ktime_get_ns() - *start_ts;
        bpf_trace_printk("Process %d exited, duration: %llu ns\\n", pid, duration);
        start.delete(&pid);
    }
    return 0;
}
"""

# Load and attach eBPF program
b = BPF(text=bpf_program)

# Define the Python class for the data structure
class Data(ct.Structure):
    _fields_ = [
        ("pid", ct.c_uint32),
        ("ppid", ct.c_uint32),
        ("start_time", ct.c_uint64),
        ("comm", ct.c_char * 16),
        ("filename", ct.c_char * 32)
    ]

# Process events
def print_event(cpu, data, size):
    event = ct.cast(data, ct.POINTER(Data)).contents
    print(f"PID: {event.pid}, PPID: {event.ppid}, Command: {event.comm.decode('utf-8')}, File: {event.filename.decode('utf-8')}")

# Loop to print events
b["events"].open_perf_buffer(print_event)
print("Tracing process executions... Press Ctrl+C to exit.")

# Print traced processes and their durations
def print_duration_event(cpu, data, size):
    event = b.trace_fields()
    print(f"Duration: {event}")

b.trace_print(print_duration_event)

try:
    while True:
        b.perf_buffer_poll()
except KeyboardInterrupt:
    print("Exiting...")

# Print statistics
print("\nTop 10 processes by execution count:")
b["start"].print_log2_hist("pid")
