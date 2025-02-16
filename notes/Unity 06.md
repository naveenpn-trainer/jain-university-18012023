# Lambda Arcitecture

> Lambda Architecture is a data processing architecture designed to handle large-scale, real-time and batch data processing

## Key Components of Lambda Architecture

1. Batch Layer (Cold Path)
2. Speed Layer (Hot Path)
3. Serving Layer

## Important Points

* It is a hybrid approach to process big data. It supports both batch and stream processing

* The key idea is to split the data processing into two different paths

  * Batch Layer
  * Streaming Layer

  

![img](https://miro.medium.com/v2/resize:fit:1165/1*Nn-rjIpPVCYgw4-LvCkK8A.png)

* Lambda architecture provides a way to handle both real-time and batch processing in a single architecture.



## Lambda Architecture

* **Ingestion** : Data is ingested into the system from various sources in real-time
* **Batch Processing** : Process historical data.
* **Real-time processing** : the speed layer processes the real-time data
* **Serving Layer** : The results from both the batch layer and streaming are stored in the serving layer.
* **Querying** : Queries from users or application for data visualization and analysis.



## Frameworks 

1. **Serving Layer**, HDFS, Cloud Storage (S3, ADLS, GCS)
2. **Stream processing** : Apache Storm, Spark (Spark Streaming, Structured Streaming), Kafka Streams, Apache Flink
3. **Batch Processing** : MapReduce (Deprecated), Apache Spark, 



## Self Study

* Kappa Architecture