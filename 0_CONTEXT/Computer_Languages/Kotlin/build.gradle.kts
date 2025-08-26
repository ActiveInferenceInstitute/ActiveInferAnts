plugins {
    kotlin("jvm") version "1.9.10"
    application
}

group = "com.activeinference"
version = "1.0.0"

repositories {
    mavenCentral()
}

dependencies {
    implementation(kotlin("stdlib"))
    implementation("org.jetbrains.kotlinx:kotlinx-coroutines-core:1.7.3")
    implementation("com.google.code.gson:gson:2.10.1")
    implementation("org.apache.commons:commons-math3:3.6.1")

    testImplementation(kotlin("test"))
}

application {
    mainClass.set("com.activeinference.MainKt")
}

tasks.jar {
    manifest {
        attributes["Main-Class"] = "com.activeinference.MainKt"
    }

    // Include dependencies in JAR
    from(configurations.runtimeClasspath.get().map { if (it.isDirectory) it else zipTree(it) })

    duplicatesStrategy = DuplicatesStrategy.EXCLUDE
}

tasks.register<JavaExec>("runSingleAgent") {
    group = "application"
    classpath = sourceSets.main.get().runtimeClasspath
    mainClass.set("com.activeinference.SingleAgentDemoKt")
}

tasks.register<JavaExec>("runAntColony") {
    group = "application"
    classpath = sourceSets.main.get().runtimeClasspath
    mainClass.set("com.activeinference.AntColonyDemoKt")
}
