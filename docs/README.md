## About the connector

The ANY.RUN Threat Intelligence Feeds connector FortiSOAR users with continuously updated, high-fidelity IOCs (malicious IPs, domains, and URLs) extracted from live sandbox analyses across 15,000+ SOCs. This enables proactive defense against emerging threats with rich context including sandbox session links for faster triage and response.

With TI Feeds, you SOC can ensure: 
- **Early threat detection** using real-time IOCs from the latest emerging malware & phishing, catching attacks hours before they hit. 
- **More effective Tier 1** as analysts will be able to resolve more alerts without escalation thanks to clear indicator context. 
- **Lightning-fast MTTR** with TTPs and behavior insights from sandbox reports, enabling automated triage and response in minutes. 

To use this connector, you need an active ANY.RUN TI Feeds subscription.

Use the Data Ingestion Wizard to easily ingest Threat Intelligence Feeds data into FortiSOAR™. For more information, see the Data Ingestion Support section.

### Version information

- Connector Version: 1.1.0
- FortiSOAR™ Version Tested on: 7.6.4-5623
- Authored By: ANY.RUN

## Release Notes for version 1.1.0

- Connector: ANY.RUN Threat Intelligence Feeds. TI Feeds provide data on the known indicators of compromise such as malicious IPs, URLs, Domains.
- Playbooks: Use the Data Ingestion Wizard to easily ingest data into FortiSOAR™ by pulling data from the ANY.RUN Threat Intelligence Feeds  using this playbook:
  - ANY.RUN Threat Intelligence Feeds > Fetch and Create


## Installing the connector

Use the Content Hub to install the connector. For the detailed procedure to install the connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector)

You can also use the following `yum` command as a root user to install connectors from an SSH session:

```bash
yum install cyops-connector-anyrun-threat-intelligence-feeds
```


## Prerequisites to configuring the connector

- Credentials are required to access the ANY.RUN Threat Intelligence Feeds server. Ensure you have an active ANY.RUN Threat Intelligence Feeds subscription. For more information about ANY.RUN Threat Intelligence Feeds, click [here](https://any.run/threat-intelligence-feeds/?utm_source=anyrungithub&utm_medium=documentation&utm_campaign=fortisoar_feeds&utm_content=linktofeeds)
- The FortiSOAR™ server should have outbound connectivity to port 443 on the ANY.RUN Threat Intelligence Feeds server.


## Configuring the connector

For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)

### Configuration parameters

In FortiSOAR™, on the Connector page, click the **ANY.RUN Threat Intelligence Feeds** connector row (if you are in the **Grid** view on the Connectors page) and in the **Configurations** tab enter the required configuration details:


| Parameter | Description |
| :-- | :-- |
| API Key | ANY.RUN API Key in format:"NS9sY..FwvfR" to access the ANY.RUN Threat Intelligence Feeds API |
| Verify SSL | Specifies whether the SSL certificate for the server is to be verified or not. By default, this option is set as True. |

### Generate API Key

- Follow [ANY.RUN](https://app.any.run/?utm_source=anyrungithub&utm_medium=documentation&utm_campaign=fortisoar&utm_content=linktoservice)
- Profile > [2] API and Limits > [3] Generate > [4] Copy

![ANYRUN_API_TOKEN.png](images/ANYRUN_API_TOKEN.png) 

## Actions supported by the connector

The following automated operations can be included in playbooks, and you can also use the annotations to access operations from FortiSOAR™:


| Function | Description | Annotation and Category |
| :-- | :-- | :-- |
| Fetch Indicators | Retrieves all available indicators of a specific collection from ANY.RUN TAXII Server based on the collection type and other input parameters you have specified. | `fetch_indicators`<br>Investigation |

### Operation: Fetch Indicators

#### Input parameters

| Parameter | Description |
| :-- | :-- |
| Collection type | Specify the type of the collection from which to retrieve the indicators. |
| Feed fetch depth | Select the period in days to retrieve indicators. |
| Process Response As | The Feed Data can either be returned as a JSON; written to a file on the FortiSOAR server; or Created as Feed Records in FortiSOAR.<br><br>**If you choose 'Create as Feed Records in FortiSOAR'**<br>- Record Creation Playbook IRI: Specify the IRI of the Record Creation Playbook in Record Creation Playbook IRI field.<br><br>**If you choose 'Return as a JSON'**<br>- No additional parameters<br><br>**If you choose 'Save to File'**<br>- Filename: Specify the name of the file in which to save the feed information, in the Filename field. |

#### Output
If you choose 'Return as a JSON', the output contains the following populated JSON schema:

```
{
  "error": "",
  "data": {
  "objects":
[
  {
    "id": "",
    "type": "",
    "labels": [],
    "created": "",
    "pattern": "",
    "revoked": "",
    "modified": "",
    "confidence": "",
    "valid_from": "",
    "pattern_type": "",
    "spec_version": "",
    "created_by_ref": "",
    "external_references": []
  }
]
      }
}
```


## Included playbooks

The `Sample - ANY.RUN Threat Intelligence Feeds - 1.1.0` playbook collection comes bundled with the ANY.RUN Threat Intelligence Feeds connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR™ after importing the ANY.RUN Threat Intelligence Feeds connector.

- > ANY.RUN Threat Intelligence Feeds > Fetch and Create
- Fetch Indicators

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection, since the sample playbook collection gets deleted during connector upgrade and delete.

## Data Ingestion Support

Use the Data Ingestion Wizard to easily ingest data into FortiSOAR™ by pulling data from the ANY.RUN Threat Intelligence Feeds. Currently, data ingested from the ANY.RUN Threat Intelligence Feeds is mapped to Threat Intel Feed in FortiSOAR™. For more information on the Data Ingestion Wizard, see the Connectors Guide in the FortiSOAR product documentation.

The Data Ingestion Wizard helps you to configure the scheduled pulling of data from ANY.RUN Threat Intelligence Feed into FortiSOAR™. It also lets you pull some sample data from ANY.RUN Threat Intelligence Feed, using which you can define the mapping of data between ANY.RUN Threat Intelligence Feed and FortiSOAR™. The mapping of common fields is generally already done by the Data Ingestion Wizard; users are mostly required to only map any custom fields that are added to the ANY.RUN Threat Intelligence Feed data.

1. To begin configuring data ingestion, click **Configure Data Ingestion** on the ANY.RUN Threat Intelligence Feeds connector's Configurations page. Click **Let's Start by fetching some data** to open the **Fetch Sample Data** screen.

![1.png](images/1.png)

2. On the **Fetch Data** screen, provide the configurations required to fetch ANY.RUN Threat Intelligence Feeds data. At this step, you can configure the following parameters:
    - **Collection Type**: Specify the type of the collection from which to retrieve the indicators
    - **Feed Fetch Date**: Select the period in days to retrieve indicators
    - **Maximum Age** (in days) to that feed
    - **TLP**

![2.png](images/2.png)

3. On the **Field Mapping** screen, map the fields of the ingested data ANY.RUN Threat Intelligence to the fields of a Threat Intel Feeds present in FortiSOAR™. To map a field, click the key in the sample data to add the Jinja value of the field.

![3.png](images/3.png)

4. Use the **Scheduling** screen to configure schedule-based ingestion, i.e., specify the polling frequency to ANY.RUN Threat Intelligence, so that the content gets pulled from integration into FortiSOAR™.
    - On the Scheduling screen, from the **Do you want to schedule the ingestion?** drop-down list, select **Yes**.
    - In the **Configure Schedule Settings** section, specify the Cron expression for the schedule.

![4.png](images/4.png)

5. The **Summary** screen displays a summary of the mapping done, and it also contains links to the Ingestion playbooks. Click **Done** to complete the data ingestion, and exit the Data Ingestion Wizard.


## Threat Intel Management Solution Pack Support

For the ingestion playbooks to work you must install and configure the Threat Intel Management Solution Pack on your FortiSOAR™ instance. For more information on solution packs, see the respective solution pack document on the Content Hub Portal.

1. To begin configuring data ingestion, click **Configure** on the Threat Intel Management Solution Pack's Configurations page. Click **Let's get started** to open the **Select Feed Integrations** screen.
   
2. Select the ANY.RUN Threat Intelligence Feeds connector from the list.

![5.png](images/5.png)


3. Provide the required configuration parameters in the Configuration Parameters field. On this step, 

![6.png](images/6.png)

4. Provide the required configuration parameters in the Ingestion Parameters field. On this step, you can configure the following parameters:
    - **Collection Type**: Specify the type of the collection from which to retrieve the indicators
    - **Feed Fetch Date**: Select the period in days to retrieve indicators
    - **Maximum Age** (in days) to that feed
    - **TLP**

![7.png](images/7.png) 

5. Use the **Ingestion Schedule** screen to configure schedule-based ingestion, i.e., specify the polling frequency to ANY.RUN Threat Intelligence, so that the content gets pulled from integration into FortiSOAR™

![8.png](images/8.png) 

6. Configure threat feed rules on Threat Feed Rules page to manage threat intelligence from sources:
 - **Linking Threat Feeds to Indicators**
 - **Ingesting Unstructured Threat Feeds**

Linking Threat Feeds to Indicators:
Enable this rule and specify a feed confidence threshold to automatically update the matching indicator record reputation from the ANY.RUN Threat Intelligence Feeds.

**Confidence Threshold**: Specify a feed confidence threshold to link feeds, with confidence threshold equal to or greater than the specified value, to the indicator.
For example, if you set this value to 75, all feeds with a confidence level equal to or greater than 75 link to the indicator and update its reputation as per the feed.

Reputation for indicators created after the feeds ingestion are updated.

![9.png](images/9.png) 

For more information, refer to the [Threat Feed Rules](https://github.com/fortinet-fortisoar/solution-pack-threat-intel-management/blob/release/3.0.0/docs/threat-feed-rules.md) document.

NOTE: Full Threat Intel Management functionality in FortiSOAR™ (e.g. Linking Threat Feeds to Indicators or Unlimited Feed Ingestion) is available if the TIM Service Subscription is enabled. For more information, see the [documentation](https://docs.fortinet.com/document/fortisoar/7.6.4/deployment-guide/223944/licensing-fortisoar#Licensing_option_for_Unrestricted_FortiGuard_Threat_Feeds_and_Advanced_Threat...).


## Support
For details on how you can make ANY.RUN's solutions a part of your infrastructure, [contact us](https://app.any.run/contact-us/?utm_source=anyrungithub&utm_campaign=fortisoar&utm_medium=documentation&utm_content=contact_us).
For technical assistance, reach out to <support@any.run>.


