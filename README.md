# Get Email Information MCP Server

## Overview

The **Get Email Information** MCP server is designed to enhance email communication efficiency by providing comprehensive validation, categorization, and enrichment of email addresses. This server not only aids in ensuring the deliverability of emails but also offers valuable demographic and descriptive data that is useful for marketing, segmentation, lead scoring, and analytics.

## Features

- **Email Validation**: Ensure that email addresses are valid and operational. This includes identifying syntax errors, detecting non-functional mail servers, and filtering out vulgar or likely bogus email addresses, which helps maintain high deliverability rates.

- **Email Categorization**: Classify email addresses by type and geography, assisting in message personalization and targeted communication strategies.

- **B2B Enrichment**: Append valuable business-related information to email addresses, such as organization descriptions, revenue, number of employees, and social media handles. This feature supports lead scoring, routing, and advanced marketing analytics.

- **Batch Processing**: High-performance batch and bulk email processing capabilities are available, enabling efficient handling of large volumes of email addresses.

## Input Parameters

- **Email**: The email address to be validated and enriched.

## Output Parameters

- **Email**: The validated email address.
- **Response**: The validation status of the email.
- **Info**: Additional information about the email.
- **Domain**: The domain associated with the email address.
- **IsGovernment**: Indicates if the email is a government (.gov) address.
- **IsEducational**: Indicates if the email is from an educational institution (.edu).
- **IsOrganizational**: Indicates if the email is from an organization (.org).
- **IsDisposable**: Identifies disposable or temporary email addresses.
- **IsVulgar**: Detects the presence of vulgarities in the email address.
- **IsGeneric**: Indicates if the email is from a generic service like Gmail, Yahoo, or Hotmail.
- **DomainOwner**: The owner of the email domain.
- **Organization**: The organization associated with the email domain.
- **Revenue**: Revenue information for the associated organization.
- **Employees**: The number of employees in the associated organization.
- **XHandle**: The organization's social media handle.
- **HeadquartersCountry**: The country where the organization's headquarters is located.
- **HeadquartersCity**: The city where the organization's headquarters is located.
- **Currency**: The currency used by the organization.
- **Rate**: The exchange rate of the currency vs USD.
- **Description**: A brief description of the organization.
- **Code**: Response code indicating the status of the operation.
- **Credits**: The number of remaining API credits.

## Tool

- **Get Email Information**:
  - **Function Name**: `get_email_information`
  - **Description**: Validates, categorizes, and enriches an email address with B2B demographics.
  - **Parameters**:
    - **email**: A sample email address (type: String).

By leveraging the **Get Email Information** MCP server, organizations can significantly improve their email communication efforts, personalize messaging strategies, and gain deeper insights into their B2B interactions. This server is an essential tool for businesses looking to optimize their email marketing and lead management strategies.