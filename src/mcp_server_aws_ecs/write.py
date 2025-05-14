from mcp.server.fastmcp import FastMCP, Context
from typing import List, Dict, Any, Optional, Union
from .common import get_ecs_client

# Write operations for AWS ECS

def register_write_tools(mcp: FastMCP):
    """
    Register all write operations (create, update, delete) for ECS with the MCP server
    
    Args:
        mcp: The FastMCP server instance
    """
    
    # Create operations
    @mcp.tool()
    def create_cluster(cluster_name: str, tags: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
        """
        Create a new ECS cluster
        
        Args:
            cluster_name: Name of the cluster to create
            tags: Optional tags to apply to the cluster
        """
        client = get_ecs_client()
        params = {"clusterName": cluster_name}
        
        if tags:
            formatted_tags = [{"key": k, "value": v} for k, v in tags.items()]
            params["tags"] = formatted_tags
            
        response = client.create_cluster(**params)
        return response.get("cluster", {})
    
    @mcp.tool()
    def create_service(
        cluster: str, 
        service_name: str,
        task_definition: str,
        desired_count: int = 1,
        launch_type: Optional[str] = None,
        platform_version: Optional[str] = None,
        scheduling_strategy: str = "REPLICA",
        deployment_configuration: Optional[Dict[str, Any]] = None,
        network_configuration: Optional[Dict[str, Any]] = None,
        load_balancers: Optional[List[Dict[str, Any]]] = None,
        service_registries: Optional[List[Dict[str, Any]]] = None,
        tags: Optional[Dict[str, str]] = None,
        enable_ecs_managed_tags: bool = False,
        propagate_tags: Optional[str] = None,
        capacity_provider_strategy: Optional[List[Dict[str, Any]]] = None
    ) -> Dict[str, Any]:
        """
        Create a new ECS service
        
        Args:
            cluster: The short name or full ARN of the cluster to run the service on
            service_name: The name of your service
            task_definition: The task definition to use with the service
            desired_count: The number of instances of the task to run
            launch_type: The launch type to use (EC2 or FARGATE)
            platform_version: The platform version to use (for FARGATE)
            scheduling_strategy: The scheduling strategy (REPLICA or DAEMON)
            deployment_configuration: Optional deployment settings
            network_configuration: Network configuration for the service
            load_balancers: The load balancers to use
            service_registries: The service discovery registries to use
            tags: Optional tags to apply to the service
            enable_ecs_managed_tags: Enable ECS managed tags
            propagate_tags: Whether to propagate tags to the tasks (TASK_DEFINITION or SERVICE)
            capacity_provider_strategy: The capacity provider strategy to use
        """
        client = get_ecs_client()
        params = {
            "cluster": cluster,
            "serviceName": service_name,
            "taskDefinition": task_definition,
            "desiredCount": desired_count,
            "schedulingStrategy": scheduling_strategy,
            "enableECSManagedTags": enable_ecs_managed_tags
        }
        
        if launch_type:
            params["launchType"] = launch_type
            
        if platform_version:
            params["platformVersion"] = platform_version
            
        if deployment_configuration:
            params["deploymentConfiguration"] = deployment_configuration
            
        if network_configuration:
            params["networkConfiguration"] = network_configuration
            
        if load_balancers:
            params["loadBalancers"] = load_balancers
            
        if service_registries:
            params["serviceRegistries"] = service_registries
            
        if tags:
            formatted_tags = [{"key": k, "value": v} for k, v in tags.items()]
            params["tags"] = formatted_tags
            
        if propagate_tags:
            params["propagateTags"] = propagate_tags
            
        if capacity_provider_strategy:
            params["capacityProviderStrategy"] = capacity_provider_strategy
            
        response = client.create_service(**params)
        return response.get("service", {})
    
    @mcp.tool()
    def create_capacity_provider(
        name: str,
        auto_scaling_group_provider: Dict[str, Any],
        tags: Optional[Dict[str, str]] = None
    ) -> Dict[str, Any]:
        """
        Create a new capacity provider
        
        Args:
            name: The name of the capacity provider
            auto_scaling_group_provider: The Auto Scaling group provider settings
            tags: Optional tags to apply to the capacity provider
        """
        client = get_ecs_client()
        params = {
            "name": name,
            "autoScalingGroupProvider": auto_scaling_group_provider
        }
        
        if tags:
            formatted_tags = [{"key": k, "value": v} for k, v in tags.items()]
            params["tags"] = formatted_tags
            
        response = client.create_capacity_provider(**params)
        return response.get("capacityProvider", {})
    
    @mcp.tool()
    def create_task_set(
        cluster: str,
        service: str,
        task_definition: str,
        external_id: Optional[str] = None,
        network_configuration: Optional[Dict[str, Any]] = None,
        load_balancers: Optional[List[Dict[str, Any]]] = None,
        service_registries: Optional[List[Dict[str, Any]]] = None,
        launch_type: Optional[str] = None,
        capacity_provider_strategy: Optional[List[Dict[str, Any]]] = None,
        platform_version: Optional[str] = None,
        scale: Optional[Dict[str, Any]] = None,
        tags: Optional[Dict[str, str]] = None
    ) -> Dict[str, Any]:
        """
        Create a task set in the specified cluster and service
        
        Args:
            cluster: The cluster where the service is running
            service: The service to create the task set in
            task_definition: The task definition for the task set
            external_id: An optional external ID to associate with the task set
            network_configuration: The network configuration for the task set
            load_balancers: A list of load balancer objects
            service_registries: The service registry entries for the task set
            launch_type: The launch type the task set will use
            capacity_provider_strategy: The capacity provider strategy to use for the task set
            platform_version: The platform version to use for the task set
            scale: A floating-point percentage of the desired number of tasks to place and keep running
            tags: Optional tags to associate with the task set
        """
        client = get_ecs_client()
        params = {
            "cluster": cluster,
            "service": service,
            "taskDefinition": task_definition
        }
        
        if external_id:
            params["externalId"] = external_id
            
        if network_configuration:
            params["networkConfiguration"] = network_configuration
            
        if load_balancers:
            params["loadBalancers"] = load_balancers
            
        if service_registries:
            params["serviceRegistries"] = service_registries
            
        if launch_type:
            params["launchType"] = launch_type
            
        if capacity_provider_strategy:
            params["capacityProviderStrategy"] = capacity_provider_strategy
            
        if platform_version:
            params["platformVersion"] = platform_version
            
        if scale:
            params["scale"] = scale
            
        if tags:
            formatted_tags = [{"key": k, "value": v} for k, v in tags.items()]
            params["tags"] = formatted_tags
            
        response = client.create_task_set(**params)
        return response.get("taskSet", {})
    
    # Delete operations
    @mcp.tool()
    def delete_cluster(cluster: str) -> Dict[str, Any]:
        """
        Delete an ECS cluster
        
        Args:
            cluster: The name or ARN of the cluster to delete
        """
        client = get_ecs_client()
        response = client.delete_cluster(cluster=cluster)
        return response.get("cluster", {})
    
    @mcp.tool()
    def delete_service(
        cluster: str,
        service: str,
        force: bool = False
    ) -> Dict[str, Any]:
        """
        Delete an ECS service
        
        Args:
            cluster: The name or ARN of the cluster that hosts the service to delete
            service: The name or ARN of the service to delete
            force: Whether to force the deletion even if the service can't be scaled down to 0
        """
        client = get_ecs_client()
        response = client.delete_service(
            cluster=cluster,
            service=service,
            force=force
        )
        return response.get("service", {})
    
    @mcp.tool()
    def delete_capacity_provider(capacity_provider: str) -> Dict[str, Any]:
        """
        Delete a capacity provider
        
        Args:
            capacity_provider: The name or ARN of the capacity provider to delete
        """
        client = get_ecs_client()
        response = client.delete_capacity_provider(capacityProvider=capacity_provider)
        return response.get("capacityProvider", {})
    
    @mcp.tool()
    def delete_account_setting(
        name: str,
        principal_arn: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Delete an account setting for a specified IAM user, IAM role, or the root user
        
        Args:
            name: The name of the account setting to delete
            principal_arn: The ARN of the principal to delete the setting for (optional)
        """
        client = get_ecs_client()
        params = {"name": name}
        
        if principal_arn:
            params["principalArn"] = principal_arn
            
        response = client.delete_account_setting(**params)
        return response.get("setting", {})
    
    @mcp.tool()
    def delete_attributes(
        cluster: str,
        attributes: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Delete attributes from an Amazon ECS resource
        
        Args:
            cluster: The cluster that contains the resource with the attributes to delete
            attributes: The attributes to delete from the resource
        """
        client = get_ecs_client()
        response = client.delete_attributes(
            cluster=cluster,
            attributes=attributes
        )
        return {
            "attributes": response.get("attributes", [])
        }
    
    @mcp.tool()
    def delete_task_set(
        cluster: str,
        service: str,
        task_set: str,
        force: bool = False
    ) -> Dict[str, Any]:
        """
        Delete a task set
        
        Args:
            cluster: The name or ARN of the cluster that hosts the service that the task set exists in
            service: The name or ARN of the service that the task set exists in
            task_set: The name or ARN of the task set to delete
            force: Whether to force the deletion even if the task set is still scaling
        """
        client = get_ecs_client()
        response = client.delete_task_set(
            cluster=cluster,
            service=service,
            taskSet=task_set,
            force=force
        )
        return response.get("taskSet", {})
    
    # Update operations
    @mcp.tool()
    def update_service(
        cluster: str,
        service: str,
        desired_count: Optional[int] = None,
        task_definition: Optional[str] = None,
        deployment_configuration: Optional[Dict[str, Any]] = None,
        network_configuration: Optional[Dict[str, Any]] = None,
        platform_version: Optional[str] = None,
        force_new_deployment: bool = False,
        health_check_grace_period_seconds: Optional[int] = None,
        capacity_provider_strategy: Optional[List[Dict[str, Any]]] = None,
        enable_execute_command: Optional[bool] = None,
        enable_ecs_managed_tags: Optional[bool] = None
    ) -> Dict[str, Any]:
        """
        Update an ECS service
        
        Args:
            cluster: The name or ARN of the cluster that hosts the service to update
            service: The name or ARN of the service to update
            desired_count: The number of instantiations of the task to place and keep running (optional)
            task_definition: The family and revision or ARN of the task definition to run (optional)
            deployment_configuration: Optional deployment parameters (optional)
            network_configuration: The network configuration for the service (optional)
            platform_version: The platform version for the service (optional)
            force_new_deployment: Whether to force a new deployment of the service (default: False)
            health_check_grace_period_seconds: The health check grace period (optional)
            capacity_provider_strategy: The capacity provider strategy to use (optional)
            enable_execute_command: Whether to enable execute command on the service (optional)
            enable_ecs_managed_tags: Whether to enable ECS managed tags (optional)
        """
        client = get_ecs_client()
        params = {
            "cluster": cluster,
            "service": service,
            "forceNewDeployment": force_new_deployment
        }
        
        if desired_count is not None:
            params["desiredCount"] = desired_count
            
        if task_definition:
            params["taskDefinition"] = task_definition
            
        if deployment_configuration:
            params["deploymentConfiguration"] = deployment_configuration
            
        if network_configuration:
            params["networkConfiguration"] = network_configuration
            
        if platform_version:
            params["platformVersion"] = platform_version
            
        if health_check_grace_period_seconds is not None:
            params["healthCheckGracePeriodSeconds"] = health_check_grace_period_seconds
            
        if capacity_provider_strategy:
            params["capacityProviderStrategy"] = capacity_provider_strategy
            
        if enable_execute_command is not None:
            params["enableExecuteCommand"] = enable_execute_command
            
        if enable_ecs_managed_tags is not None:
            params["enableECSManagedTags"] = enable_ecs_managed_tags
            
        response = client.update_service(**params)
        return response.get("service", {})
    
    @mcp.tool()
    def update_task_protection(
        cluster: str,
        tasks: List[str],
        protection_enabled: bool,
        expires_in_minutes: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        Update the protection status of a task
        
        Args:
            cluster: The short name or ARN of the cluster that hosts the service 
            tasks: A list of up to 10 task IDs or ARNs
            protection_enabled: Specify True to mark a task for protection, False to unset it
            expires_in_minutes: Duration for task protection in minutes (1-2880) (optional)
        """
        client = get_ecs_client()
        params = {
            "cluster": cluster,
            "tasks": tasks,
            "protectionEnabled": protection_enabled
        }
        
        if expires_in_minutes is not None:
            params["expiresInMinutes"] = expires_in_minutes
            
        response = client.update_task_protection(**params)
        return {
            "protectedTasks": response.get("protectedTasks", []),
            "failures": response.get("failures", [])
        }
    
    @mcp.tool()
    def update_task_set(
        cluster: str,
        service: str,
        task_set: str,
        scale: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Update a task set
        
        Args:
            cluster: The short name or ARN of the cluster that hosts the service
            service: The short name or ARN of the service that the task set exists in
            task_set: The short name or ARN of the task set to update
            scale: A floating-point percentage of the desired number of tasks to place and keep running
        """
        client = get_ecs_client()
        response = client.update_task_set(
            cluster=cluster,
            service=service,
            taskSet=task_set,
            scale=scale
        )
        return response.get("taskSet", {})
    
    @mcp.tool()
    def run_task(
        cluster: str,
        task_definition: str,
        count: int = 1,
        group: Optional[str] = None,
        network_configuration: Optional[Dict[str, Any]] = None,
        overrides: Optional[Dict[str, Any]] = None,
        placement_constraints: Optional[List[Dict[str, Any]]] = None,
        placement_strategy: Optional[List[Dict[str, Any]]] = None,
        platform_version: Optional[str] = None,
        enable_ecs_managed_tags: bool = False,
        propagate_tags: Optional[str] = None,
        reference_id: Optional[str] = None,
        started_by: Optional[str] = None,
        tags: Optional[Dict[str, str]] = None,
        enable_execute_command: Optional[bool] = None,
        capacity_provider_strategy: Optional[List[Dict[str, Any]]] = None,
        launch_type: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Run a task on your cluster
        
        Args:
            cluster: The name or ARN of the cluster to run the task on
            task_definition: The task definition to use
            count: The number of instantiations of the task to run (default: 1)
            group: The name of the task group to associate with the task
            network_configuration: The network configuration for the task
            overrides: A list of container overrides
            placement_constraints: Placement constraints for the task
            placement_strategy: Placement strategies for the task
            platform_version: The platform version the task should run on
            enable_ecs_managed_tags: Whether to enable ECS managed tags
            propagate_tags: Whether to propagate tags from the task definition or service
            reference_id: The reference ID to use for the task
            started_by: An optional tag to associate with the task
            tags: Optional tags to associate with the task
            enable_execute_command: Whether to enable execute command for the task
            capacity_provider_strategy: The capacity provider strategy to use
            launch_type: The launch type to use (EC2 or FARGATE)
        """
        client = get_ecs_client()
        params = {
            "cluster": cluster,
            "taskDefinition": task_definition,
            "count": count,
            "enableECSManagedTags": enable_ecs_managed_tags
        }
        
        if group:
            params["group"] = group
            
        if network_configuration:
            params["networkConfiguration"] = network_configuration
            
        if overrides:
            params["overrides"] = overrides
            
        if placement_constraints:
            params["placementConstraints"] = placement_constraints
            
        if placement_strategy:
            params["placementStrategy"] = placement_strategy
            
        if platform_version:
            params["platformVersion"] = platform_version
            
        if propagate_tags:
            params["propagateTags"] = propagate_tags
            
        if reference_id:
            params["referenceId"] = reference_id
            
        if started_by:
            params["startedBy"] = started_by
            
        if tags:
            formatted_tags = [{"key": k, "value": v} for k, v in tags.items()]
            params["tags"] = formatted_tags
            
        if enable_execute_command is not None:
            params["enableExecuteCommand"] = enable_execute_command
            
        if capacity_provider_strategy:
            params["capacityProviderStrategy"] = capacity_provider_strategy
            
        if launch_type:
            params["launchType"] = launch_type
            
        response = client.run_task(**params)
        return response.get("tasks", [])
    
    @mcp.tool()
    def stop_task(
        cluster: str,
        task: str,
        reason: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Stop a running task
        
        Args:
            cluster: The name or ARN of the cluster that hosts the task to stop
            task: The task ID or ARN of the task to stop
            reason: An optional reason for stopping the task
        """
        client = get_ecs_client()
        params = {
            "cluster": cluster,
            "task": task
        }
        
        if reason:
            params["reason"] = reason
            
        response = client.stop_task(**params)
        return response.get("task", {})
    
    @mcp.tool()
    def register_task_definition(
        family: str,
        container_definitions: List[Dict[str, Any]],
        execution_role_arn: Optional[str] = None,
        network_mode: Optional[str] = None,
        task_role_arn: Optional[str] = None,
        volumes: Optional[List[Dict[str, Any]]] = None,
        placement_constraints: Optional[List[Dict[str, Any]]] = None,
        requires_compatibilities: Optional[List[str]] = None,
        cpu: Optional[str] = None,
        memory: Optional[str] = None,
        tags: Optional[Dict[str, str]] = None,
        pid_mode: Optional[str] = None,
        ipc_mode: Optional[str] = None,
        proxy_configuration: Optional[Dict[str, Any]] = None,
        runtime_platform: Optional[Dict[str, Any]] = None,
        ephemeral_storage: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Register a new task definition
        
        Args:
            family: The family name for the task definition
            container_definitions: A list of container definitions
            execution_role_arn: The ARN of the task execution role
            network_mode: The Docker networking mode for the containers
            task_role_arn: The ARN of the role the containers can assume
            volumes: A list of volume definitions for the task
            placement_constraints: A list of placement constraints
            requires_compatibilities: The launch types the task definition is compatible with
            cpu: The CPU units for the task
            memory: The memory for the task
            tags: Optional tags to associate with the task definition
            pid_mode: The process namespace to use for the containers
            ipc_mode: The IPC resource namespace to use for the containers
            proxy_configuration: The configuration details for the App Mesh proxy
            runtime_platform: The operating system that your tasks are running on
            ephemeral_storage: The amount of ephemeral storage to allocate for the task
        """
        client = get_ecs_client()
        params = {
            "family": family,
            "containerDefinitions": container_definitions
        }
        
        if execution_role_arn:
            params["executionRoleArn"] = execution_role_arn
            
        if network_mode:
            params["networkMode"] = network_mode
            
        if task_role_arn:
            params["taskRoleArn"] = task_role_arn
            
        if volumes:
            params["volumes"] = volumes
            
        if placement_constraints:
            params["placementConstraints"] = placement_constraints
            
        if requires_compatibilities:
            params["requiresCompatibilities"] = requires_compatibilities
            
        if cpu:
            params["cpu"] = cpu
            
        if memory:
            params["memory"] = memory
            
        if tags:
            formatted_tags = [{"key": k, "value": v} for k, v in tags.items()]
            params["tags"] = formatted_tags
            
        if pid_mode:
            params["pidMode"] = pid_mode
            
        if ipc_mode:
            params["ipcMode"] = ipc_mode
            
        if proxy_configuration:
            params["proxyConfiguration"] = proxy_configuration
            
        if runtime_platform:
            params["runtimePlatform"] = runtime_platform
            
        if ephemeral_storage:
            params["ephemeralStorage"] = ephemeral_storage
            
        response = client.register_task_definition(**params)
        return response.get("taskDefinition", {})
    
    @mcp.tool()
    def deregister_task_definition(
        task_definition: str
    ) -> Dict[str, Any]:
        """
        Deregister a task definition
        
        Args:
            task_definition: The family and revision or ARN of the task definition to deregister
        """
        client = get_ecs_client()
        response = client.deregister_task_definition(taskDefinition=task_definition)
        return response.get("taskDefinition", {})
