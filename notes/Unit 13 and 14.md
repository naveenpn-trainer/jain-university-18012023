# Data Ingestion into Big Data System

A Data Lake is a centralized storage repository used to store large amounts of structured, semi-structured and unstructured data.

![img](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcjOdYJKV8QYlXVi8Jpv-kJi6PA2zggTTQ5pGOlp15RhoIaVD8dwaN0lg9EFa3Ah5L8ByoRvMP_K5TEvhXHOzX6Ocgy5d1OxRTnC-JkO3bcpTf6u_siaZ1ZLcDXUu7xlI3WrKLz59N8tFGuJTzYqdCi00Wx?key=Xt0A5xy6197aqF7pI2sZxQ)

## Frameworks to Ingestion Data

![img](https://lh7-rt.googleusercontent.com/docsz/AD_4nXd66yyVaqEmYXclz2XXuc3t71Z4Dim6YLhm-WPkDBKjWRBwxkCtj9MhjlLUAPanrWz5EWrEzJzIb-NLp1cZ4VxSMcsBC3haTQEeIkd2FQGqNzidintn94BY06AG0MGRKcnQJRQfmQtK-shUY9oO4icTrjKQ?key=Xt0A5xy6197aqF7pI2sZxQ)



> Apache Sqoop is a Data Ingestion tool designed to transferring bulk data between structured sources (RDBMS) to Hadoop and vice-versa

![img](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfLygm6sW_M8eUT760rmnwHVW94Ws9DfPM5a1e5ZdRUQ4A--LmxI7fegDw7FWCaZ3fSOcQN3TEylb3gs-R874hSxljjc1yzbp5kvD6Y5TPBdH6HhwQ23KSPziw_s1SDNvDDjocXvIb-eiuzIb5FCFdAnRQn?key=vtFsYFjhJ6GS0W0_NFClcg)

## Apache Flume

> Apache Flume is Data Ingestion tool/framework to ingest large volumes of data data from multiple sources into a centralized data stores like HDFS, HBase, Kafka

### Common Data Sources

![img](https://lh7-rt.googleusercontent.com/docsz/AD_4nXetjOdGfmghnrcPNkJJKyn9NfI4_svZ609PbDl-B5091CkvohS83alCD64TVtJdIGV5sCpbvvuyWvpk_4MMMiflcyQ2IrxEwKlSiB0w8OXIiE0Wwez4cW0gstuPsQG8PSE30DmKZ7BMCDhkXjOtYJa7cIGS?key=DW0DGb_9Xrfqijr4AjgtVA)

### Components of Flume

1. Source : Collects data from an external system (Netcat, Spooling Directory, Kafka)
2. Channel : Acts as a buffer between source and sink (E.g MemoryChannel, FileChannel)
3. Sink : Delivers the data to a final destination (HDFS, HBase, Kafka)
4. Agent : Java Process that configures and hosts the source, channel and sink

### Data Flow

Source --> Channel --> Sink

### Use Cases

1. Streaming Logs from Web servers to HDFS
2. Collecting events from IoT devices
3. Ingesting files from a spooling directory into HDFS

### Flume Sources

![img](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdbW0NFkbCGJwExwLPtfT5x39kItV_5kCWKjcUj1l1KlLaH3vLFNzTsiD_eQoW4XrEw4CODeQWepCxoaBdLPNv2r5hS2lCTNmQMXI0hFrelDvMR0hFQYy_B2VhuXn1eu3uN2J9IWF2HUSWzIMqAHoDriOo?key=DW0DGb_9Xrfqijr4AjgtVA)

### Flume Agent Configuration (Skeleton)

```
# Define the agent and its source, channels and Sink
agent.sources = mySource
agent.channels = myChannel
agent.sinks = MySink

# Source Configuration



# Channel COnfiguration


# SInk COnfiguration


# Bind the source and sink to the channel
```

### Hands-on Demo

#### Streaming Text Data from Netcat to HDFS

net_cat_to_hdfs.config

```
# Define the agent and its source, channels and Sink
NetCatAgent.sources=Netcat
NetCatAgent.channels=FileChannel
NetCatAgent.sinks=HdfsSink

# Source Configuration
NetCatAgent.sources.Netcat.type=netcat
NetCatAgent.sources.Netcat.bind=localhost
NetCatAgent.sources.Netcat.port=56525

# Channel COnfiguration
NetCatAgent.channels.FileChannel.type=file
NetCatAgent.channels.FileChannel.dataDirs=/home/naveenpn/NetCatAgent/dataDirs
NetCatAgent.channels.FileChannel.checkpointDir=/home/naveenpn/NetCatAgent/checkpointDir

# Sink COnfiguration
NetCatAgent.sinks.HdfsSink.type=hdfs
NetCatAgent.sinks.HdfsSink.hdfs.path=/user/naveenpn/netcat
NetCatAgent.sinks.HdfsSink.hdfs.fileSuffix=.log
NetCatAgent.sinks.HdfsSink.hdfs.writeFormat=Text

# Bind the source and sink to the channel
NetCatAgent.sources.Netcat.channels=FileChannel
NetCatAgent.sinks.HdfsSink.channel=FileChannel

```

**Command to run**

```
flume-ng agent -n NetCatAgent -f net_cat_to_hdfs.config
```

**Command to start netcat (New terminal)**

```
nc localhost 56527
```

#### Streaming Data From File

spool_directory_to_hdfs.config

```
# Define the agent
SpoolDirectoryAgent.sources = mysource
SpoolDirectoryAgent.sinks = mysink
SpoolDirectoryAgent.channels = mychannel

# Channel Configuration
SpoolDirectoryAgent.channels.mychannel.type = memory

# Source Configuration
SpoolDirectoryAgent.sources.mysource.type = spooldir
SpoolDirectoryAgent.sources.mysource.spoolDir = /home/naveenpn/incoming

# Sink Configuration
SpoolDirectoryAgent.sinks.mysink.type = hdfs
SpoolDirectoryAgent.sinks.mysink.hdfs.path = /flume_output
SpoolDirectoryAgent.sinks.mysink.hdfs.writeFormat = Text
SpoolDirectoryAgent.sinks.mysink.hdfs.fileType =  DataStream


# Bind the source and sink to the channel
SpoolDirectoryAgent.sources.mysource.channels = mychannel
SpoolDirectoryAgent.sinks.mysink.channel = mychannel


```

flume-ng agent -n SpoolDirectoryAgent -f spool_directory_to_hdfs.config
