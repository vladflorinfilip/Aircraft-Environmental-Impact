# Environmental Impact Evaluation of Aircraft Design and Flight Specifications

This project leverages the Breguet equation to evaluate the environmental impact of varying aircraft design and flight specifications, focusing on CO₂ and NOₓ emissions across different altitudes, flight ranges, and design choices. The analysis includes comparisons for a standard jet-powered Boeing 787-8 and a hydrogen-powered retrofit A320, examining the trade-offs between operational efficiency and environmental impact.

## Project Overview

This project investigates two main areas:

1. **Flight Altitude Optimization:**
Varying flight altitude to optimize fuel burn per payload range, analyzing CO₂ and NOₓ emissions.
A short-haul route (London to Bucharest) and a long-haul route (London to Bogota) are examined to study altitude step changes for different ranges.

2. **Overall Pressure Ratio (OPR) Impact:**
Studying the impact of the overall pressure ratio on emissions to guide efficient aircraft design.
The analysis considers the total global warming potential, balancing design and operational adjustments.

Additionally, the feasibility of a hydrogen-powered aircraft operating at equatorial routes is evaluated, focusing on modifications that minimize contrail formation and CO₂ emissions.

## Key Findings

1. **Altitude Analysis**
- CO₂ Emissions: Decrease with increasing altitude.
- NOₓ Emissions: Initially decrease but then rise as the tropopause is surpassed.
- Environmental Impact: Higher altitudes exacerbate the impact of NOₓ emissions due to increased ozone lifetime.
- Velocity Ratio: A velocity ratio near unity helps minimize the combined CO₂ and NOₓ emissions.
- Altitude Stepping: Shows minor reductions in emissions, with limited impact on overall emissions.
- Design vs. Environmental Impact: A balance is needed between optimal economic design and minimized environmental impact, especially for different ranges.

2. **Overall Pressure Ratio (OPR) Analysis**
- Lower OPR at Lower Altitudes: Results in reduced environmental impact.
- Higher OPR for High Altitudes: Can improve efficiency but only up to a certain threshold in terms of environmental benefit.

3. **Hydrogen-Powered Aircraft Analysis**
- For equatorial routes, a retrofitted A320 hydrogen-powered aircraft demonstrated a reduced environmental footprint:
- Range: Achieves a 1,500 km range with 87 passengers.
- CO₂ Emissions: Reduced to zero through hydrogen power.
- Contrail Formation: Minimized by operating at 6,000 m altitude.
- NOₓ Emissions: Reduced by optimized design and operation.

## Getting Started

### Prerequisites
To run the code, ensure you have:

- Python 3.x installed
- Required packages, which can be installed via:
`pip install -r requirements.txt`

### Usage
Setting Up the Flight and Design Parameters: Modify parameters within the code, including:
- Flight altitude
- Overall pressure ratio
- Range and payload specifications for the B787-8 and hydrogen-powered A320.

### Output: 
The program will output:
- CO₂ and NOₓ emissions for different altitudes and pressure ratios.
- Global warming potential for specified configurations.

## Results Interpretation

The code outputs environmental impact metrics for various configurations:

- CO₂ Emissions: Total emissions based on payload range and fuel burn rate.
- NOₓ Emissions: Estimated based on flight altitude and pressure ratios.
- Global Warming Potential: A cumulative metric that balances CO₂ and NOₓ impact.

## Acknowledgements

This project was created by Vlad Filip for the A7 course at the Department of Engineering, University of Cambridge.
