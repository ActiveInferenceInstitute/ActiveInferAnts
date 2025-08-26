const std = @import("std");

const ActiveInferenceAgent = struct {
    const Self = @This();

    num_states: usize = 4,
    num_observations: usize = 3,
    num_actions: usize = 2,
    beliefs: [4]f64,
    a_matrix: [3][3]f64,
    b_matrix: [2][2]f64,
    c_vector: [3]f64,
    d_vector: [2]f64,
    allocator: std.mem.Allocator,

    pub fn init(allocator: std.mem.Allocator) Self {
        return Self{
            .beliefs = [_]f64{0.25, 0.25, 0.25, 0.25},
            .a_matrix = [_][3]f64{
                [_]f64{0.8, 0.1, 0.1},
                [_]f64{0.1, 0.8, 0.1},
                [_]f64{0.1, 0.1, 0.8},
            },
            .b_matrix = [_][2]f64{
                [_]f64{0.9, 0.1},
                [_]f64{0.1, 0.9},
            },
            .c_vector = [_]f64{0.0, 0.5, 0.0},
            .d_vector = [_]f64{0.5, 0.5},
            .allocator = allocator,
        };
    }

    pub fn updateBeliefs(self: *Self, observation: usize) void {
        const likelihood = self.a_matrix[observation - 1];
        var posterior: [4]f64 = undefined;
        var total: f64 = 0.0;

        // Calculate posterior P(s|o) ∝ P(o|s) * P(s)
        for (likelihood, self.beliefs, 0..) |l, b, i| {
            posterior[i] = l * b;
            total += posterior[i];
        }

        // Normalize
        if (total > 0.0) {
            for (&posterior, 0..) |*p, i| {
                p.* = posterior[i] / total;
            }
            self.beliefs = posterior;
        }
    }

    pub fn calculateExpectedFreeEnergy(self: *Self, action: usize) f64 {
        var efe: f64 = 0.0;
        for (self.beliefs) |belief| {
            if (belief > 0.0) {
                efe -= belief * @log(belief);
            }
        }
        return efe;
    }

    pub fn selectAction(self: *Self) usize {
        var min_efe: f64 = std.math.inf_f64;
        var best_action: usize = 1;

        var action: usize = 1;
        while (action <= self.num_actions) : (action += 1) {
            const efe = self.calculateExpectedFreeEnergy(action);
            if (efe < min_efe) {
                min_efe = efe;
                best_action = action;
            }
        }

        return best_action;
    }

    pub fn step(self: *Self, observation: usize) usize {
        self.updateBeliefs(observation);
        return self.selectAction();
    }

    pub fn printBeliefs(self: *Self) void {
        std.debug.print("Beliefs: ", .{});
        for (self.beliefs, 0..) |belief, i| {
            std.debug.print("{d:.3}", .{belief});
            if (i < self.beliefs.len - 1) {
                std.debug.print(", ", .{});
            }
        }
        std.debug.print("\n", .{});
    }
};

pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    defer _ = gpa.deinit();
    const allocator = gpa.allocator();

    std.debug.print("Zig Active Inference Demo\n", .{});

    var agent = ActiveInferenceAgent.init(allocator);
    std.debug.print("Initial ", .{});
    agent.printBeliefs();

    var cycle: usize = 1;
    while (cycle <= 5) : (cycle += 1) {
        const observation = (cycle - 1) % 3 + 1;
        const action = agent.step(observation);
        std.debug.print("Cycle {}: Observation={}, Action={}, ", .{cycle, observation, action});
        agent.printBeliefs();
    }
}
