# Introduction to Big Data

> Big Data refers to the data which is **large, fast** and complex type of **structured, semi-structured and unstructured data** generated from variety of different sources, which becomes difficult to store and process using a traditional processing system.

**Challenges of Big Data**

1. Storage : Distributed Storage System
2. Processing : MPP (Massive Parallel Processing Framework)

## Hadoop 2.x (Distributed Storage and Processing System)

> Apache Hadoop is a software framework that allows us to **store and process large datasets** in parallel and distributed fashion

## Components of Hadoop 2.x

1. Storage Layer : HDFS (Hadoop Distributed FS)
2. Cluster Manager : YARN (Yet Another Resource Negotiator)
3. Data Processing Layer : MapReduce

![img](https://lh7-rt.googleusercontent.com/docsz/AD_4nXe-_e4iuG56dzx6yCFc00HhYzhfS69UCS9VShowz4Exx8Gf08n1fZsaaJ2TCbe7-Sw6MdO7BqKdQ4CtZQGdiAh79gqaJhMbP8KXwuubv3gGOtwvwifUwIH-txbTmqFTvdwj6mbTqtRoybnR19soafR0fJ_U?key=Lcjgu0sLjm8U8i3A_14gRg)

## Hadoop Daemon Services

* A daemon service refers to a long running background process or service that performs various tasks to support components of Hadoop.

![img](https://lh7-rt.googleusercontent.com/docsz/AD_4nXda6z7P8U6DC4B1SgFtZssdeLpJUXoP81CvuthCPEyO7bv8YWd6LJZ5Erc3Nb7yJRr3BZN3UwITJO9TeLAJsWxMbQvfkjXIvi-QUGeOgTuCSVlhG265L0UMQCd2BriX81NLxSEPpCaTtelbGhuVMWiaj0Q?key=Lcjgu0sLjm8U8i3A_14gRg)

## Master Slave Architecture

![img](https://lh7-rt.googleusercontent.com/docsz/AD_4nXe_0umPg0HG348JZ9K_oaSZUPdnzZ2Mr7K3DVN_F-cIM8dYIGi0g1xn-J-1XEAwnB9lyySrTxNjOPkUMkrHGcPARZ0wx7x4KNboZQSudwei84aX9mR5-gIGLWcr1N_jYlH-23tiPX2N2jgNFkCuEuRFYL1Y?key=Lcjgu0sLjm8U8i3A_14gRg)

## HDFS and Architecture

> HDFS is a **Distributed and Scalable File System** designed for storing very large files.

**Distributed**

* In HDFS, files are stored across multiple machines. HDFS splits the file into smaller chunks (Blocks)

<img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXemDtIw73rk-SGBVq-a40l3O0rcM_Glr7ivBvkDRwBVLSLEoPkEK1a8xbg898ySqUuG5fLG_E4Ti-lnk_1nI6qx79kQPyZMu0NaVnK06jb5HpihH-totAZqt9bzPRDCBgeuSczu-sedPB7r0aOkxZ_nespj?key=Lcjgu0sLjm8U8i3A_14gRg" alt="img" style="zoom:50%;" />

**Scalable**

* I can increase or decrease the number of nodes in the cluster



















