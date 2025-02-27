
---

### 7. **docs/coffee_scenario.md**

```markdown
# Coffee Scenario: Traceability Journey

This document details the coffee traceability scenario implemented in the agripilot traceability module.

## Scenario Overview

1. **Harvested:**  
   - **Location:** Jammu Farm  
   - **Description:** Coffee beans are harvested by local farmers.

2. **Processed:**  
   - **Location:** Mumbai Processor  
   - **Description:** Harvested beans are processed into coffee powder.

3. **Packaged:**  
   - **Location:** Mumbai Facility  
   - **Description:** Processed coffee powder is packaged for distribution.

4. **Shipped:**  
   - **Location:** Pune Distribution Center  
   - **Description:** Packaged coffee is shipped to Pune.

5. **Delivered:**  
   - **Location:** Pune Retailer  
   - **Description:** Coffee reaches a retail outlet in Pune.

6. **Served:**  
   - **Location:** Pune Cafe  
   - **Description:** The coffee powder is used in a milkshake, completing the journey.

## API Integration

- **/api/update:** Records each stage update.  
- **/api/track:** Retrieves the complete journey using a Beckn-like response format.
