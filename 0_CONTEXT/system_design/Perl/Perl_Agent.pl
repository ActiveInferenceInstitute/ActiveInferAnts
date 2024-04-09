#!/usr/bin/perl

use strict;
use warnings;
use List::Util qw(sum);

# Define agent states, perceptions, and actions
use constant {
    STATE_IDLE       => 'idle',
    STATE_PROCESSING => 'processing',
    STATE_ACTING     => 'acting',
    PERCEPTION_SIGNAL   => 'signal_detected',
    PERCEPTION_OBSTACLE => 'obstacle_detected',
    PERCEPTION_CLEAR    => 'path_clear',
    ACTION_WAIT     => 'wait',
    ACTION_MOVE     => 'move',
    ACTION_INTERACT => 'interact',
};

my @states      = (STATE_IDLE, STATE_PROCESSING, STATE_ACTING);
my @perceptions = (PERCEPTION_SIGNAL, PERCEPTION_OBSTACLE, PERCEPTION_CLEAR);
my @actions     = (ACTION_WAIT, ACTION_MOVE, ACTION_INTERACT);

# Define the Bayesian graph for each state
my %agent_graphs = (
    STATE_IDLE() => {
        external_states => {PERCEPTION_SIGNAL() => 0.2, PERCEPTION_OBSTACLE() => 0.1, PERCEPTION_CLEAR() => 0.7},
        action_states   => {ACTION_WAIT() => 0.7, ACTION_MOVE() => 0.2, ACTION_INTERACT() => 0.1},
        sense_states    => {STATE_PROCESSING() => 0.3, STATE_ACTING() => 0.1, STATE_IDLE() => 0.6},
        internal_states => {STATE_IDLE() => 0.9, STATE_PROCESSING() => 0.1},
    },
    STATE_PROCESSING() => {
        external_states => {PERCEPTION_SIGNAL() => 0.6, PERCEPTION_OBSTACLE() => 0.1, PERCEPTION_CLEAR() => 0.3},
        action_states   => {ACTION_WAIT() => 0.1, ACTION_MOVE() => 0.4, ACTION_INTERACT() => 0.5},
        sense_states    => {STATE_PROCESSING() => 0.5, STATE_ACTING() => 0.4, STATE_IDLE() => 0.1},
        internal_states => {STATE_PROCESSING() => 0.8, STATE_ACTING() => 0.2},
    },
    STATE_ACTING() => {
        external_states => {PERCEPTION_SIGNAL() => 0.1, PERCEPTION_OBSTACLE() => 0.4, PERCEPTION_CLEAR() => 0.5},
        action_states   => {ACTION_WAIT() => 0.2, ACTION_MOVE() => 0.6, ACTION_INTERACT() => 0.2},
        sense_states    => {STATE_PROCESSING() => 0.2, STATE_ACTING() => 0.7, STATE_IDLE() => 0.1},
        internal_states => {STATE_ACTING() => 0.9, STATE_IDLE() => 0.1},
    },
);

# Active Inference Agent
package ActiveInferenceAgent;

sub new {
    my ($class, $initial_state) = @_;
    my $self = {
        current_state => $initial_state,
    };
    bless $self, $class;
    return $self;
}

sub update_state {
    my ($self) = @_;
    my $internal_probabilities = $agent_graphs{$self->{current_state}}{internal_states};
    my $r = rand();
    my $cumulative_prob = 0;
    foreach my $state (keys %$internal_probabilities) {
        $cumulative_prob += $internal_probabilities->{$state};
        if ($r <= $cumulative_prob) {
            $self->{current_state} = $state;
            last;
        }
    }
}

sub perceive_event {
    my ($self) = @_;
    my $external_probabilities = $agent_graphs{$self->{current_state}}{external_states};
    my $r = rand();
    my $cumulative_prob = 0;
    foreach my $perception (keys %$external_probabilities) {
        $cumulative_prob += $external_probabilities->{$perception};
        if ($r <= $cumulative_prob) {
            return $perception;
        }
    }
    return PERCEPTION_CLEAR();
}

sub decide_action {
    my ($self) = @_;
    my $action_probabilities = $agent_graphs{$self->{current_state}}{action_states};
    my $r = rand();
    my $cumulative_prob = 0;
    foreach my $action (keys %$action_probabilities) {
        $cumulative_prob += $action_probabilities->{$action};
        if ($r <= $cumulative_prob) {
            return $action;
        }
    }
    return ACTION_WAIT();
}

# Simulate agent behavior
sub simulate_agent_behavior {
    my ($num_iterations) = @_;
    my $agent = ActiveInferenceAgent->new(STATE_IDLE());
    
    for (my $i = 0; $i < $num_iterations; $i++) {
        my $perception = $agent->perceive_event();
        my $action = $agent->decide_action();
        print "Iteration $i: Perception: $perception, Action: $action\n";
        $agent->update_state();
    }
}

# Run the simulation
simulate_agent_behavior(10);
