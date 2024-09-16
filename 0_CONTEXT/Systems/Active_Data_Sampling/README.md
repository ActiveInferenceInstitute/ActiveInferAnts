Here's a comprehensive markdown README summarizing the Active Inference Active Data Sampling (ADS) model and associated package:

# Active Inference Active Data Sampling (ADS)

## Overview

Active Data Sampling (ADS) is an approach to optimizing data selection and experimental design based on principles from active inference and information theory. The key ideas are:

1. Use a generative model to predict data and quantify uncertainty
2. Calculate expected information gain for potential data samples
3. Select samples that maximize information gain while considering costs
4. Update model beliefs after each new observation
5. Repeat this cycle to efficiently gather informative data

This approach allows for intelligent, adaptive sampling that can reduce computational and experimental costs compared to exhaustive or random sampling.

## Key Concepts

- **Generative Model**: Specifies prior beliefs and likelihood of data given hidden states/parameters
- **Expected Information Gain**: Quantifies anticipated change in beliefs from new observations  
- **Message Passing**: Efficient inference in graphical models
- **Trade-off**: Balance between information seeking and costs/preferences

## Mathematical Framework

The core equations for ADS include:

1. Expected information gain:
   ```
   I[π] = E[DKL[p(θ|y,π) || p(θ|π)]]
        = DKL[p(y,θ|π) || p(θ|π)p(y|π)]
        = E[ln p(y|θ,π)] - E[ln p(y|π)]
   ```

2. Message passing form:
   ```
   I[π]^i = Λ_i[μ_i^pa(i) Λ_y[μ_i^ch(i) ln μ_i^ch(i)]] - Λ_y[μ_y^pa(y) ln μ_y^pa(y)]
   ```

3. Trade-off with costs:
   ```
   G = [I[π], 0] + C
   ```

## Package Features

The ADS package provides:

1. Core ADS algorithm implementation
2. Visualization tools for:
   - Active sampling cycles
   - Information gain landscapes
   - Belief updates
   - Sampling choices over time
3. Templates for common use cases:
   - Function approximation
   - Dynamic process tracking  
   - Clinical trial design
4. Extensible framework for custom generative models

## Usage Examples

### Function Approximation

```python
import ads

# Define generative model
model = ads.GaussianBasisModel(num_basis=16)

# Run ADS
results = ads.run_ads(model, num_samples=28, cost=0.25)

# Visualize
ads.plot_function_approximation(results)
```

### Clinical Trial

```python
import ads

# Define trial model  
model = ads.ClinicalTrialModel()

# Run ADS with survival preference
results = ads.run_ads(model, num_cohorts=16, survival_preference=True)

# Visualize
ads.plot_trial_results(results)
```

## Key Visualizations

The package generates visualizations including:

- Information gain vs sampling choice
- Inferred function with uncertainty
- Sampling locations over time  
- Posterior parameter estimates
- Survival curves for clinical trials

## Extensions

Potential extensions include:

- Sophisticated recursive planning
- Empirical validation tools
- Custom cost function design
- Integration with large-scale ML pipelines

## References

[1] Parr, T., Friston, K., & Zeidman, P. (2024). Active Data Selection and Information Seeking. Algorithms, 17(3), 118.

[2] Friston, K. J., et al. (2017). Active inference, curiosity and insight. Neural computation, 29(10), 2633-2683.

This README provides an overview of the ADS approach and associated package. Refer to the full documentation for detailed API references and advanced usage.

Citations:
[1] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/343060/e76bdd80-db39-4906-8b90-60c7f9ec3695/algorithms-17-00118-v2.pdf
[2] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/343060/6863b5cd-3637-482f-a6f7-ca142d1c1d76/algorithms-17-00118.xml
[3] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/343060/e05076ee-b9df-4bff-9a01-e4333ea003f3/algorithms-17-00118.epub
[4] https://www.mdpi.com/1999-4893/17/3/118