<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method="xml" encoding="UTF-8" indent="yes"/>

<xsl:template match="/">
	
<xsl:comment> OBS-ExclusiveArch: aarch64 x86_64 </xsl:comment>
<xsl:comment>
                This file is generated,
                don't manually modify this file,
                please check README
</xsl:comment>

<image schemaversion="6.9" name="ceph-csi-image" xmlns:suse_label_helper="com.suse.label_helper">

  <description type="system">
    <author>Denis Kondratenko</author>
    <contact>denis.kondratenko@suse.com</contact>
    <specification>Ceph CSI driver container</specification>
  </description>

  <preferences>
    <type image="docker">
      <xsl:attribute name="derived_from">
        <xsl:value-of select="param/image" />
      </xsl:attribute>
      <containerconfig
        tag="latest"
        additionaltags="%PKG_VERSION%.%PKG_COMMIT_NUM%.%RELEASE%,%PKG_VERSION%.%PKG_COMMIT_NUM%"
        maintainer="SUSE Storage Team &lt;bgardner@suse.com&gt;">
        <xsl:attribute name="name">
          <xsl:value-of select="param/name" />
        </xsl:attribute>

        <entrypoint execute="/usr/bin/cephcsi"/>

         <labels>

          <suse_label_helper:add_prefix>
            <xsl:attribute name="prefix">
              <xsl:value-of select="param/prefix" />
            </xsl:attribute>

            <label name="org.opencontainers.image.title">
              <xsl:attribute name="value">
                <xsl:value-of select="param/title" />
              </xsl:attribute>
            </label>

            <label name="org.opencontainers.image.description" value="Ceph CSI driver"/>
            <label name="org.opencontainers.image.version" value="%PKG_VERSION%.%PKG_COMMIT_NUM%"/>
            <label name="org.opencontainers.image.created" value="%BUILDTIME%"/>
            <label name="org.opencontainers.image.vendor" value="SUSE LLC"/>

            <label name="org.opencontainers.image.url">
              <xsl:attribute name="value">
                <xsl:value-of select="param/url" />
              </xsl:attribute>
            </label>            

            <label name="org.openbuildservice.disturl" value="%DISTURL%"/>

            <label name="org.opensuse.reference">
              <xsl:attribute name="value">
                <xsl:value-of select="param/reference" />
              </xsl:attribute>
            </label> 
          
          </suse_label_helper:add_prefix>

          <xsl:for-each select="param/labels/label">
            <label>
              <xsl:attribute name="name">
                <xsl:value-of select="name" />
              </xsl:attribute>
              <xsl:attribute name="value">
                <xsl:value-of select="value" />
              </xsl:attribute>
            </label>
          </xsl:for-each>

        </labels>

        <history author="Denis Kondratenko &lt;denis.kondratenko@suse.com&gt;">New Ceph CSI image</history>
     </containerconfig>
    </type>
    <version>1.0.0</version>
    <packagemanager>zypper</packagemanager>
    <rpm-check-signatures>false</rpm-check-signatures>
    <rpm-excludedocs>true</rpm-excludedocs>
    <locale>en_US</locale>
    <keytable>us.map.gz</keytable>
  </preferences>

  <repository type='rpm-md'>
    <source path='obsrepositories:/'/>
  </repository>

  <packages type="image">
    <package name="ceph-csi"/>

    <xsl:for-each select="param/packages_image/package">
      <package>
        <xsl:attribute name="name">
          <xsl:value-of select="name" />
        </xsl:attribute>
      </package>
    </xsl:for-each>

  </packages>

  <packages type='bootstrap'>
    <package name='filesystem'/>
    <package name='glibc-locale-base'/>

    <xsl:for-each select="param/packages_boot/package">
      <package>
        <xsl:attribute name="name">
          <xsl:value-of select="name" />
        </xsl:attribute>
      </package>
    </xsl:for-each>

  </packages>

</image>

</xsl:template>

</xsl:stylesheet> 
