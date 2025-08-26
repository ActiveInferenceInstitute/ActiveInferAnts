# Active Inference Implementation in Perl

This directory contains a dynamic Perl implementation of active inference with text processing capabilities and CPAN ecosystem integration.

## Overview

The Perl implementation provides:
- Dynamic typing and runtime flexibility
- Rich text processing for data analysis
- Extensive CPAN module ecosystem
- Regular expression pattern matching

## Core Components

- **Perl_Agent.pl**: Main active inference agent implementation

## Architecture

### Perl-Specific Features
The implementation leverages Perl's unique features:

- **Regular Expressions**: Pattern matching for observation processing
- **Dynamic Typing**: Flexible data structure handling
- **CPAN Modules**: Extensive library ecosystem
- **Text Processing**: Built-in string manipulation capabilities

### Agent Structure
```perl
package ActiveInference::Agent;

sub new {
    my ($class, %args) = @_;
    return bless {
        beliefs => {},
        observations => [],
        actions => [],
        precision => 1.0,
        learning_rate => 0.1
    }, $class;
}
```

## Dependencies

- Perl 5.20+
- Standard Perl distribution
- Optional CPAN modules:
  - `Math::Matrix` for matrix operations
  - `Statistics::Distributions` for probability calculations
  - `JSON` for data serialization
  - `Getopt::Long` for command-line processing

## Installing Dependencies

```bash
# Install CPAN modules
cpan Math::Matrix Statistics::Distributions JSON Getopt::Long
```

## Building and Running

```bash
# Run the implementation
perl Perl_Agent.pl

# With command-line options
perl Perl_Agent.pl --states 4 --observations 3 --steps 100

# With debugging
perl -d Perl_Agent.pl
```

## Configuration

The implementation supports flexible configuration:

```perl
my %config = (
    num_states => 4,
    num_observations => 3,
    num_actions => 2,
    learning_rate => 0.1,
    precision => 1.0,
    uncertainty_weight => 0.1,
    max_iterations => 100,
    convergence_threshold => 1e-6,
    output_format => 'json'
);
```

## Core Algorithms

### Belief Update with Regular Expressions
```perl
sub update_beliefs {
    my ($self, $observation) = @_;

    # Pattern matching for observation processing
    if ($observation =~ /pattern/) {
        # Update beliefs based on pattern match
        $self->{beliefs}->{$1} *= $self->{learning_rate};
    }

    # Normalize beliefs
    $self->_normalize_beliefs();
}
```

### Free Energy Calculation
```perl
sub calculate_free_energy {
    my ($self) = @_;

    my $free_energy = 0;
    foreach my $state (keys %{$self->{beliefs}}) {
        my $belief = $self->{beliefs}->{$state};
        $free_energy -= $belief * log($belief) if $belief > 0;
    }

    return $free_energy;
}
```

## Text Processing Capabilities

### Observation Processing
```perl
sub process_observation {
    my ($self, $text_input) = @_;

    # Regular expression patterns for different observation types
    my @patterns = (
        qr/food/i,
        qr/danger/i,
        qr/safe/i,
        qr/unknown/i
    );

    foreach my $pattern (@patterns) {
        if ($text_input =~ $pattern) {
            return $self->_create_observation($pattern, $1);
        }
    }
}
```

### Natural Language Processing
- **Pattern Recognition**: Regex-based observation classification
- **Text Analysis**: String manipulation for belief updates
- **Data Extraction**: Parsing structured and unstructured text
- **Report Generation**: Text-based result formatting

## Performance Characteristics

### Dynamic Features
- **Runtime Flexibility**: Dynamic method dispatch
- **Memory Efficiency**: Automatic garbage collection
- **Fast Prototyping**: Quick development cycles
- **Text Processing**: Optimized string operations

### Ecosystem Integration
- **CPAN Modules**: 25,000+ available modules
- **Database Integration**: DBI for data persistence
- **Web Integration**: CGI and web frameworks
- **System Administration**: Text processing automation

## Output and Analysis

The implementation generates:
- Text-based belief state reports
- JSON-formatted results
- CSV data exports
- HTML visualization reports

## Extensions

### Advanced Features
- **Natural Language Processing**: Advanced text analysis
- **Web Integration**: CGI and web application interfaces
- **Database Persistence**: Long-term data storage
- **System Monitoring**: Log analysis and processing

### Integration Options
- **Bioinformatics**: Sequence analysis and pattern matching
- **System Administration**: Log processing and automation
- **Data Analysis**: Text mining and information extraction
- **Web Development**: Content processing and generation

## References

### Key Papers
1. **Friston, K. (2010)**: The free-energy principle: a unified brain theory?
2. **Da Costa, L., et al. (2020)**: Active inference on discrete state-spaces
3. **Parr, T., & Friston, K. (2019)**: Generalised free energy and active inference

### Perl Resources
1. **Modern Perl**: Best practices and modern techniques
2. **Programming Perl**: Comprehensive language reference
3. **Perl Cookbook**: Practical solutions and examples
