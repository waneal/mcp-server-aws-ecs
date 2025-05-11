from mcp.server.fastmcp import FastMCP, Context
import boto3
import os
from typing import List, Dict, Any, Optional, Union

# Get AWS authentication credentials from environment variables
aws_profile = os.environ.get("AWS_PROFILE")
# aws_access_key_id = os.environ.get("AWS_ACCESS_KEY_ID")
# aws_secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY")
# aws_session_token = os.environ.get("AWS_SESSION_TOKEN")
aws_region = os.environ.get("AWS_REGION", "ap-northeast-1")  # Default is Tokyo region

# Create MCP server
mcp = FastMCP("AWS ECS MCP Server")

# Initialize ECS client
def get_ecs_client():
    session = boto3.Session(
        profile_name=aws_profile,
#        aws_access_key_id=aws_access_key_id,
#        aws_secret_access_key=aws_secret_access_key,
#        aws_session_token=aws_session_token,
        region_name=aws_region
    )
    return session.client('ecs')

# ---- ECS Tools ----

@mcp.tool()
def list_clusters() -> List[str]:
    """
    Get a list of available ECS clusters
    """
    client = get_ecs_client()
    response = client.list_clusters()
    return response.get('clusterArns', [])

@mcp.tool()
def describe_service(cluster_arn: str, service_arn: str) -> List[Dict[str, Any]]:
    """
    Get detailed information for a specific service

    Args:
        cluster_arn: ARN of the cluster
        service_arn: ARN of the service
    """
    client = get_ecs_client()
    response = client.describe_services(cluster=cluster_arn, services=[service_arn])
    return response.get('services', [])

@mcp.tool()
def list_services(cluster_arn: str) -> List[str]:
    """
    List services within a specified cluster

    Args:
        cluster_arn: ARN of the cluster
    """
    client = get_ecs_client()
    response = client.list_services(cluster=cluster_arn)
    return response.get('serviceArns', [])

@mcp.tool()
def list_tasks(cluster_arn: str, service_arn: Optional[str] = None) -> List[str]:
    """
    List tasks within a specified cluster
    Optional filtering by service is available

    Args:
        cluster_arn: ARN of the cluster
        service_arn: ARN of the service (optional)
    """
    client = get_ecs_client()
    params = {'cluster': cluster_arn}

    if service_arn:
        params['serviceName'] = service_arn

    response = client.list_tasks(**params)
    return response.get('taskArns', [])

@mcp.tool()
def describe_tasks(cluster_arn: str, task_arns: List[str]) -> List[Dict[str, Any]]:
    """
    Get detailed information for the specified tasks

    Args:
        cluster_arn: ARN of the cluster
        task_arns: List of task ARNs
    """
    client = get_ecs_client()
    response = client.describe_tasks(cluster=cluster_arn, tasks=task_arns)
    return response.get('tasks', [])

@mcp.tool()
def list_task_definitions() -> List[str]:
    """
    Get a list of registered task definitions
    """
    client = get_ecs_client()
    response = client.list_task_definitions()
    return response.get('taskDefinitionArns', [])

@mcp.tool()
def list_container_instances(cluster_arn: str) -> List[str]:
    """
    List container instances within a specified cluster

    Args:
        cluster_arn: ARN of the cluster
    """
    client = get_ecs_client()
    response = client.list_container_instances(cluster=cluster_arn)
    return response.get('containerInstanceArns', [])

@mcp.tool()
def describe_container_instances(cluster_arn: str, container_instance_arns: List[str]) -> List[Dict[str, Any]]:
    """
    Get detailed information for the specified container instances

    Args:
        cluster_arn: ARN of the cluster
        container_instance_arns: List of container instance ARNs
    """
    client = get_ecs_client()
    response = client.describe_container_instances(
        cluster=cluster_arn,
        containerInstances=container_instance_arns
    )
    return response.get('containerInstances', [])

@mcp.tool()
def list_account_settings(effective_settings: bool = True, principal_arn: Optional[str] = None) -> List[Dict[str, Any]]:
    """
    List account settings for the AWS account

    Args:
        effective_settings: Whether to return only effective settings (default: True)
        principal_arn: ARN of IAM user, role, or root user to return settings for (optional)
    """
    client = get_ecs_client()
    params = {'effectiveSettings': effective_settings}

    if principal_arn:
        params['principalArn'] = principal_arn

    response = client.list_account_settings(**params)
    return response.get('settings', [])

@mcp.tool()
def list_attributes(cluster_arn: Optional[str] = None, target_type: Optional[str] = None,
                   attribute_name: Optional[str] = None, attribute_value: Optional[str] = None) -> List[Dict[str, Any]]:
    """
    List attributes of ECS resources

    Args:
        cluster_arn: ARN of the cluster (optional)
        target_type: Target type of the attribute (e.g., container-instance) (optional)
        attribute_name: Filter by attribute name (optional)
        attribute_value: Filter by attribute value (optional)
    """
    client = get_ecs_client()
    params = {}

    if cluster_arn:
        params['cluster'] = cluster_arn
    if target_type:
        params['targetType'] = target_type
    if attribute_name:
        params['attributeName'] = attribute_name
    if attribute_value:
        params['attributeValue'] = attribute_value

    response = client.list_attributes(**params)
    return response.get('attributes', [])

@mcp.tool()
def list_capacity_providers() -> List[str]:
    """
    Get a list of available capacity providers
    """
    client = get_ecs_client()
    response = client.list_capacity_providers()
    return response.get('capacityProviderArns', [])

@mcp.tool()
def describe_capacity_providers(capacity_provider_arns: List[str]) -> List[Dict[str, Any]]:
    """
    Get detailed information for the specified capacity providers

    Args:
        capacity_provider_arns: List of capacity provider ARNs
    """
    client = get_ecs_client()
    response = client.describe_capacity_providers(capacityProviders=capacity_provider_arns)
    return response.get('capacityProviders', [])

@mcp.tool()
def list_task_definition_families(family_prefix: Optional[str] = None, status: str = "ACTIVE") -> List[str]:
    """
    List task definition families

    Args:
        family_prefix: Filter by family name prefix (optional)
        status: Task definition status, either ACTIVE or INACTIVE (default: ACTIVE)
    """
    client = get_ecs_client()
    params = {'status': status}

    if family_prefix:
        params['familyPrefix'] = family_prefix

    response = client.list_task_definition_families(**params)
    return response.get('families', [])

@mcp.tool()
def list_tags_for_resource(resource_arn: str) -> Dict[str, str]:
    """
    List tags associated with the specified resource

    Args:
        resource_arn: ARN of the resource to get tags for
    """
    client = get_ecs_client()
    response = client.list_tags_for_resource(resourceArn=resource_arn)
    tags_list = response.get('tags', [])

    # Convert list of tags to dictionary format
    tags_dict = {tag['key']: tag['value'] for tag in tags_list}
    return tags_dict

@mcp.tool()
def describe_clusters(cluster_arns: List[str]) -> List[Dict[str, Any]]:
    """
    Get detailed information for multiple clusters at once

    Args:
        cluster_arns: List of cluster ARNs
    """
    client = get_ecs_client()
    response = client.describe_clusters(clusters=cluster_arns)
    return response.get('clusters', [])

@mcp.tool()
def describe_services(cluster_arn: str, service_arns: List[str]) -> List[Dict[str, Any]]:
    """
    Get detailed information for multiple services at once

    Args:
        cluster_arn: ARN of the cluster
        service_arns: List of service ARNs
    """
    client = get_ecs_client()
    response = client.describe_services(cluster=cluster_arn, services=service_arns)
    return response.get('services', [])

@mcp.tool()
def describe_task_sets(cluster_arn: str, service_arn: str, task_sets: Optional[List[str]] = None) -> List[Dict[str, Any]]:
    """
    Get detailed information for task sets within a specified service

    Args:
        cluster_arn: ARN of the cluster
        service_arn: ARN of the service
        task_sets: List of task set ARNs (optional)
    """
    client = get_ecs_client()
    params = {
        'cluster': cluster_arn,
        'service': service_arn
    }

    if task_sets:
        params['taskSets'] = task_sets

    response = client.describe_task_sets(**params)
    return response.get('taskSets', [])

@mcp.tool()
def get_cluster_capacity_providers(cluster_arn: str) -> Dict[str, Any]:
    """
    Get capacity providers and default strategy associated with a cluster

    Args:
        cluster_arn: ARN of the cluster
    """
    client = get_ecs_client()
    cluster_details = client.describe_clusters(
        clusters=[cluster_arn],
        include=['ATTACHMENTS', 'SETTINGS', 'CONFIGURATIONS', 'STATISTICS']
    )

    clusters = cluster_details.get('clusters', [])
    if not clusters:
        return {
            'capacityProviders': [],
            'defaultCapacityProviderStrategy': []
        }

    cluster = clusters[0]
    return {
        'capacityProviders': cluster.get('capacityProviders', []),
        'defaultCapacityProviderStrategy': cluster.get('defaultCapacityProviderStrategy', [])
    }

@mcp.tool()
def list_services_with_details(cluster_arn: str) -> List[Dict[str, Any]]:
    """
    List services in a cluster and get detailed information for each service

    Args:
        cluster_arn: ARN of the cluster
    """
    client = get_ecs_client()

    # Get list of services
    services_arns = []
    next_token = None

    while True:
        params = {'cluster': cluster_arn}
        if next_token:
            params['nextToken'] = next_token

        response = client.list_services(**params)
        services_arns.extend(response.get('serviceArns', []))

        next_token = response.get('nextToken')
        if not next_token:
            break

    # Process in batches as we can only get details for max 10 services at once
    all_services = []
    batch_size = 10

    for i in range(0, len(services_arns), batch_size):
        batch = services_arns[i:i + batch_size]
        if batch:
            details = client.describe_services(cluster=cluster_arn, services=batch)
            all_services.extend(details.get('services', []))

    return all_services

@mcp.tool()
def get_task_protection(cluster_arn: str, task_arns: List[str]) -> List[Dict[str, Any]]:
    """
    Get protection settings for the specified tasks

    Args:
        cluster_arn: ARN of the cluster
        task_arns: List of task ARNs
    """
    client = get_ecs_client()
    response = client.get_task_protection(cluster=cluster_arn, tasks=task_arns)
    return response.get('protectedTasks', [])

@mcp.tool()
def list_service_deployments(service_arn: str, max_results: Optional[int] = None) -> List[Dict[str, Any]]:
    """
    List deployments for a service

    Args:
        service_arn: ARN of the service
        max_results: Maximum number of results to return (optional)
    """
    client = get_ecs_client()
    params = {'service': service_arn}

    if max_results:
        params['maxResults'] = max_results

    response = client.list_service_deployments(**params)
    return response.get('deploymentIds', [])

@mcp.tool()
def describe_service_deployments(deployment_ids: List[str]) -> List[Dict[str, Any]]:
    """
    Get detailed information for service deployments

    Args:
        deployment_ids: List of deployment IDs
    """
    client = get_ecs_client()
    response = client.describe_service_deployments(deploymentIds=deployment_ids)
    return response.get('deployments', [])

@mcp.tool()
def describe_service_revisions(cluster_arn: str, service_arn: str, revision_ids: Optional[List[str]] = None) -> List[Dict[str, Any]]:
    """
    Get detailed information about service revisions

    Args:
        cluster_arn: ARN of the cluster
        service_arn: ARN of the service
        revision_ids: List of revision IDs (optional)
    """
    client = get_ecs_client()
    params = {
        'cluster': cluster_arn,
        'service': service_arn
    }

    if revision_ids:
        params['revisionIds'] = revision_ids

    response = client.describe_service_revisions(**params)
    return response.get('revisions', [])

@mcp.tool()
def list_services_by_namespace(namespace: str, max_results: Optional[int] = None) -> List[str]:
    """
    List services associated with the specified namespace

    Args:
        namespace: Name or ARN of the namespace
        max_results: Maximum number of results to return (optional)
    """
    client = get_ecs_client()
    params = {'namespace': namespace}

    if max_results:
        params['maxResults'] = max_results

    response = client.list_services_by_namespace(**params)
    return response.get('serviceArns', [])

@mcp.tool()
def discover_poll_endpoint(cluster_arn: Optional[str] = None,
                          container_instance: Optional[str] = None) -> Dict[str, Any]:
    """
    Get the polling endpoint for the Amazon ECS agent
    Note: This API is used internally by the ECS agent

    Args:
        cluster_arn: Cluster ARN (optional)
        container_instance: Container instance ARN (optional)
    """
    client = get_ecs_client()
    params = {}

    if cluster_arn:
        params['cluster'] = cluster_arn
    if container_instance:
        params['containerInstance'] = container_instance

    response = client.discover_poll_endpoint(**params)
    return {
        'endpoint': response.get('endpoint', ''),
        'telemetryEndpoint': response.get('telemetryEndpoint', ''),
        'serviceConnectEndpoint': response.get('serviceConnectEndpoint', '')
    }

@mcp.tool()
def describe_task_definition(task_definition: str, include: Optional[List[str]] = None) -> Dict[str, Any]:
    """
    Get detailed information about a task definition

    Args:
        task_definition: The family and revision (family:revision) or full ARN of the task definition
        include: Specifies whether to see the resource tags for the task definition (optional)
    """
    client = get_ecs_client()
    params = {'taskDefinition': task_definition}
    
    if include:
        params['include'] = include
    
    response = client.describe_task_definition(**params)
    result = {}
    
    # Extract relevant fields from the response
    for key in ['taskDefinition', 'tags', 'compatibilities', 'registeredAt', 'registeredBy', 'deregisteredAt']:
        if key in response:
            result[key] = response[key]
    
    return result

# Launch server
if __name__ == "__main__":
    mcp.run()
