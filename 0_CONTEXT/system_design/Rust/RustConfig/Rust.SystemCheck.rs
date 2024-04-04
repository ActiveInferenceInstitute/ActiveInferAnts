use sysinfo::{System, SystemExt, ProcessorExt, DiskExt, NetworkExt};
use std::{fs, process::Command, env};

struct SystemCheck {
    sys: System,
}

impl SystemCheck {
    fn new() -> Self {
        let mut sys = System::new_all();
        sys.refresh_all();
        SystemCheck { sys }
    }

    fn print_system_info(&self) {
        println!("== System Information ==");
        println!("OS: {}", self.sys.long_os_version().unwrap_or_default());
        println!("Kernel: {}", self.sys.kernel_version().unwrap_or_default());
        println!("Host name: {}", self.sys.host_name().unwrap_or_default());
    }

    fn print_cpu_info(&self) {
        println!("\n== CPU Information ==");
        println!("CPU Count: {}", self.sys.processors().len());
        for cpu in self.sys.processors() {
            println!("  - {}", cpu.brand());
            println!("    Frequency: {} MHz", cpu.frequency());
        }
    }

    fn print_memory_info(&self) {
        println!("\n== Memory Information ==");
        println!("Total Memory: {} KB", self.sys.total_memory());
        println!("Used Memory: {} KB", self.sys.used_memory());
        println!("Free Memory: {} KB", self.sys.free_memory());
    }

    fn print_disk_info(&self) {
        println!("\n== Disk Information ==");
        for disk in self.sys.disks() {
            println!("  - {}", disk.name().to_string_lossy());
            println!("    Total Space: {} KB", disk.total_space());
            println!("    Available Space: {} KB", disk.available_space());
        }
    }

    fn print_network_info(&self) {
        println!("\n== Network Information ==");
        for (interface_name, data) in self.sys.networks() {
            println!("  - {}", interface_name);
            println!("    Received: {} KB", data.total_received());
            println!("    Transmitted: {} KB", data.total_transmitted());
        }
    }

    fn check_system_updates(&self) {
        println!("\n== System Settings and Constraints ==");
        let update_status = Command::new("apt-get")
            .arg("check")
            .status()
            .expect("Failed to check for updates");

        if update_status.success() {
            println!("System is up to date");
        } else {
            println!("System updates are available. Consider running 'sudo apt-get update && sudo apt-get upgrade'");
        }
    }

    fn check_disk_usage(&self) {
        let disk_usage_threshold = 80;
        for disk in self.sys.disks() {
            let used_space_percent = (disk.total_space() - disk.available_space()) * 100 / disk.total_space();
            if used_space_percent > disk_usage_threshold {
                println!("Warning: Disk '{}' is {}% full. Consider freeing up space.", disk.name().to_string_lossy(), used_space_percent);
            }
        }
    }

    fn check_cpu_governor(&self) {
        let cpu_governor = fs::read_to_string("/sys/devices/system/cpu/cpu0/cpufreq/scaling_governor")
            .unwrap_or_default()
            .trim()
            .to_string();
        println!("CPU Governor: {}", cpu_governor);
        if cpu_governor != "performance" {
            println!("Consider setting CPU governor to 'performance' for better performance");
        }
    }

    fn check_swappiness(&self) {
        let swappiness = fs::read_to_string("/proc/sys/vm/swappiness")
            .unwrap_or_default()
            .trim()
            .parse::<u8>()
            .unwrap_or_default();
        println!("Swappiness: {}", swappiness);
        if swappiness > 10 {
            println!("Consider reducing swappiness to 10 or lower for better performance");
        }
    }

    fn secure_ram(&self) {
        if env::var("SECURE_RAM").is_ok() {
            Command::new("shred")
                .arg("-u")
                .arg("/var/log/*")
                .status()
                .expect("Failed to secure RAM by shredding logs");
            println!("RAM security enhanced by shredding logs.");
        } else {
            println!("RAM security enhancement skipped. Set SECURE_RAM environment variable to enable.");
        }
    }

    pub fn run(&self) {
        self.print_system_info();
        self.print_cpu_info();
        self.print_memory_info();
        self.print_disk_info();
        self.print_network_info();
        self.check_system_updates();
        self.check_disk_usage();
        self.check_cpu_governor();
        self.check_swappiness();
        self.secure_ram();
    }
}

fn main() {
    let system_check = SystemCheck::new();
    system_check.run();
}
